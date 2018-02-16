import numpy as np
import cv2

#define nothing
def nothing(x):
    pass
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('Image')

# Create Trackbars
cv2.createTrackbar('R','Image',0,255,nothing)
cv2.createTrackbar('G','Image',0,255,nothing)
cv2.createTrackbar('B','Image',0,255,nothing)

#Create Switch
switch='0:Off\n1:On'
cv2.createTrackbar(switch,'Image',0,1,nothing)


while (1):
    cv2.imshow('Image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
    r = cv2.getTrackbarPos('R','Image')
    g = cv2.getTrackbarPos('G','Image')
    b = cv2.getTrackbarPos('B','Image')
    s = cv2.getTrackbarPos(switch,'Image')
    print r,g,b,s
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
        
        
cv2.destroyAllWindows()
