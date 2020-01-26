from __future__ import division
import io
import socket
import struct
import time
import picamera
import picamera.array
import cv2
import numpy as np
import Adafruit_PCA9685

pwm=Adafruit_PCA9685.PCA9685()
servo_min = 145
servo_max=650
slope=int((servo_max-servo_min)/180)
init_angley=150
init_anglex=30
final_angley=200
final_anglex=180
cangley=init_angley
canglex=init_anglex
step=2
timestep=0.2
dirxny=1


def set_servo_angle(angle):
    pulse_width=servo_min+slope*angle
    return pulse_width

def move_servo(channel, angle):
    pwm.set_pwm(channel,0,set_servo_angle(angle))
    #time.sleep(0.1)
    return
move_servo(8,init_angley)
move_servo(0,init_anglex)

pwm.set_pwm_freq(60)
client_socket = socket.socket()
client_socket.connect(('192.168.0.131', 8000))
connection = client_socket.makefile('wb')
print('Connected..')

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
                    height,width,channels=final.shape
                    midheight=int(height/2)
                    midwidth=int(width/2)
                    final=cv2.line(final,(0,midheight),(width,midheight),(0,255,0),1)
                    final=cv2.line(final,(midwidth,0),(midwidth,height),(0,255,0),1)
                    #image=image[:,:,::-1]
                    #cv2.imshow('Test',im2)
                    delx=int(midwidth-int(x))
                    dely=int(midheight-int(y))
                
                print("x :"+str(int(x))+", y :"+str(int(y))+", delta-x :"+ str(delx)+", delta-y :"+str(dely))
                image_stream=cv2.imencode('.jpeg',final)[1].tostring()
                stream2=io.BytesIO()
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
                
                if (dely>5):
                    dirxny=-1
                    cangley=cangley+dirxny*step
                    move_servo(8,cangley)
                elif (dely<-5):
                    dirxny=1
                    cangley=cangley+dirxny*step
                    move_servo(8,cangley)
                elif (delx>5):
                    dirxnx=1
                    canglex=canglex+dirxnx*step
                    move_servo(0,canglex)
                elif (delx<-5):
                    dirxnx=-1
                    canglex=canglex+dirxnx*step
                    move_servo(0,canglex)
                else : 
                    break            
    connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    client_socket.close()
    cv2.destroyAllWindows()
    print('Games Over')
