import numpy as np
import cv2
cap=cv2.VideoCapture(0)
#cv2.namedWindow('Trackers')
#def nothing(x):
 #   pass

#cv2.createTrackbar('LG','Trackers',0,255,nothing)
#cv2.createTrackbar('UG','Trackers',0,255,nothing)
#cv2.createTrackbar('kernelopen','Trackers',0,10,nothing)
#cv2.createTrackbar('kernelclose','Trackers',0,10,nothing)
#cv2.createTrackbar('Contour','Trackers',0,10,nothing)
#KO=cv2.getTrackbarPos('kernelopen','Trackers')
#KC=cv2.getTrackbarPos('kernelclose','Trackers')
kernel_open = np.ones((6,6),np.uint8)
kernel_closing = np.ones((12,12),np.uint8)
while True:
    ret,im=cap.read()
    #cv2.imshow('Original1',im)
    
    
    hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    LG=np.array([50,82,50])
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
    
    #im3=cv2.drawContours(im, contours, cv2.getTrackbarPos('Contour','Trackers'), (0,255,0),3)
    if (len(contours)!=0):
        
        areas = [cv2.contourArea(c) for c in contours]
        max_index=np.argmax(areas)
        cnt=contours[max_index]
        (x,y),radius = cv2.minEnclosingCircle(cnt)
        center = (int(x),int(y))
        radius = int(radius)
        final = cv2.circle(im,center,radius,(0,255,0),2)
        cv2.imshow('final',final)
        k=cv2.waitKey(1)
        if k==27:
           break
cv2.destroyAllWindows()
cap.release()
        
  
    #if cv2.waitKey(10) & 0xFF ord='q':
     #   cv2.destroyAllWindows()
     #   cap.release()
        
