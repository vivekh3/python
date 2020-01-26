import io
import socket
import struct
import time
import picamera
import numpy as np
import cv2

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
#client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#client_socket.connect(('192.168.0.110', 5000))

# Make a file-like object out of the connection
#connection = client_socket.makefile('wb')
kernel_open = np.ones((6,6),np.uint8)
kernel_closing = np.ones((12,12),np.uint8)
try:
    camera = picamera.PiCamera()
    camera.resolution = (320, 240)
    camera.framerate = 30
    camera.hflip=True
    camera.vflip=True	   
 # Start a preview and let the camera warm up for 2 seconds
    camera.start_preview()
    time.sleep(2)

    # Note the start time and construct a stream to hold image data
    # temporarily (we could write it directly to connection but in this
    # case we want to find out the size of each capture first to keep
    # our protocol simple)
    #start = time.time()
    stream = io.BytesIO()
    for foo in camera.capture_continuous(stream, 'jpeg',use_video_port=True):
        # Write the length of the capture to the stream and flush to
        # ensure it actually gets sent
        #connection.write(struct.pack('<L', stream.tell()))
        #connection.flush()
        # Rewind the stream and send the image data over the wire
        stream.seek(0)
        im=np.asarray(bytearray(stream.read()),dtype='uint8')
        im=cv2.imdecode (im,cv2.IMREAD_COLOR)

        hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
        LG=np.array([38,94,74])
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
        #cv2.imshow('dilation',dilation)
        im2,contours, hierarchy = cv2.findContours(dilation2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    #im3=cv2.drawContours(im, contours, cv2.getTrackbarPos('Contour','Trackers'), (0,255,0),3)
        if (len(contours)!=0):
        
            areas = [cv2.contourArea(c) for c in contours]
            max_index=np.argmax(areas)
            cnt=contours[max_index]

            (x,y),radius = cv2.minEnclosingCircle(cnt)
            center = (int(x),int(y))
            radius = int(radius)
            final = cv2.circle(im,center,radius,(0,255,0),2)
            height,width,channels=final.shape
            midheight=int(height/2)
            midwidth=int(width/2)

            cv2.line(final,(0,midheight),(width,midheight),(0,255,0),2)
            cv2.line(final,(midwidth,0),(midwidth,height),(0,255,0),2)
    
            #font = cv2.FONT_HERSHEY_SIMPLEX
            centerTxt= "("+str(int(x-midwidth))+","+str(int(y-midheight))+")"
            print (centerTxt)
            #cv2.putText(final,centerTxt,(int(x),int(y)),font,0.5,(255,255,255),2,cv2.LINE_AA)
        

            cv2.imshow('final',final)
            time.sleep(0.4)

            #cv2.imshow('Image', image)
        #connection.write(stream.read())
        # If we've been capturing for more than 30 seconds, quit
        # Reset the stream for the next capture
            stream.seek(0)
            stream.truncate()
            k=cv2.waitKey(1)
            if k==27:
               break
    # Write a length of zero to the stream to signal we're done
    #connection.write(struct.pack('<L', 0))
finally:
        cv2.destroyAllWindows()
        
     #   connection.close()
 #   client_socket.close()

