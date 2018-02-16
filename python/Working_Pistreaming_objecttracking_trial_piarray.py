import io
import socket
import struct
import time
import picamera
import picamera.array
import cv2
import numpy as np


client_socket = socket.socket()
client_socket.connect(('192.168.0.131', 8000))
connection = client_socket.makefile('wb')
kernel_open = np.ones((6,6),np.uint8)
kernel_closing = np.ones((12,12),np.uint8)

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (320,240)
        camera.framerate = 60
        camera.vflip=True
        camera.hflip=True
        time.sleep(2)
        start = time.time()
        stream = io.BytesIO()
        #print(type(stream))
        # Use the video-port for captures...
        while (True):
            with picamera.array.PiRGBArray(camera) as stream:
                camera.capture(stream,format='rgb')
                im=stream.array
                hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
                LG=np.array([50,215,50])
                UG=np.array([255,255,255])
                mask=cv2.inRange(hsv,LG,UG)
                closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_closing)
                erosion=cv2.erode(closing,kernel_open,iterations=1)
                #cv2.imshow('erosion',erosion)
    
                blur=cv2.GaussianBlur(erosion,(15,15),0)
                #cv2.imshow('blur',blur)
                ret,thres1=cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
                #cv2.imshow('threshold',thres1)
                dilation=cv2.dilate(thres1,kernel_open,iterations=2)
                erosion2=cv2.erode(dilation,kernel_open,iterations=1)
                dilation2=cv2.dilate(erosion,kernel_open,iterations=3)
                
                im2,contours, hierarchy = cv2.findContours(dilation2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
                if (len(contours)!=0):
        
                    areas = [cv2.contourArea(c) for c in contours]
                    max_index=np.argmax(areas)
                    cnt=contours[max_index]
                    (x,y),radius = cv2.minEnclosingCircle(cnt)
                    center = (int(x),int(y))
                    radius = int(radius)
                    final = cv2.circle(im,center,radius,(0,255,0),2)
                #for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                    #data = np.fromstring(stream.getvalue(), dtype=np.uint8)
                    #image=cv2.imdecode(data,1)
                        #height,width,channels=image.shape
                        #midheight=int(height/2)
                        #midwidth=int(width/2)
                        #im2=cv2.line(image,(0,midheight),(width,midheight),(0,255,0),2)
                        #im2=cv2.line(im2,(midwidth,0),(midwidth,height),(0,255,0),2)
                        #image=image[:,:,::-1]
                #cv2.imshow('Test',final)
                image_stream=cv2.imencode('.jpeg',final)[1].tostring()
                stream2=io.BytesIO()
            #print(type(image_stream))
                stream2.write(image_stream)
                #print(type(stream2))
                connection.write(struct.pack('<L', stream2.tell()))
                connection.flush()
                stream2.seek(0)
                connection.write(stream2.read())
                #if time.time() - start > 60:
                #    break
                k=cv2.waitKey(1)
                if k==27:
                   break
                stream2.seek(0)
                stream2.truncate()
    connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    client_socket.close()
    cv2.destroyAllWindows()
    print('Games Over')
