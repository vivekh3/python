import numpy as np
import cv2
cap=cv2.VideoCapture(0)
#define nothing
def nothing(x):
    pass
#blueball = 103,128,47
#greenball = 38,94,74
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('Image')

# Create Trackbars
cv2.createTrackbar('H','Image',0,255,nothing)
cv2.createTrackbar('S','Image',0,255,nothing)
cv2.createTrackbar('V','Image',0,255,nothing)

kernel_open = np.ones((6,6),np.uint8)
kernel_closing = np.ones((12,12),np.uint8)

while (1):
    ret,im=cap.read()
    hsv_im=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    Upper=np.array([255,255,255])
    cv2.imshow('Image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
    h = cv2.getTrackbarPos('H','Image')
    s = cv2.getTrackbarPos('S','Image')
    v = cv2.getTrackbarPos('V','Image')
    Lower=np.array([h,s,v])
    print Lower
    mask=cv2.inRange(hsv_im,Lower,Upper)

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
    cv2.imshow('dilation',dilation2)
    cv2.imshow('mask',mask)
        
cv2.destroyAllWindows()
cap.release()
