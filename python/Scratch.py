import numpy
import cv2

Image = cv2.imread("Arrows\slide1.jpg")

height,width,channels=Image.shape
print (height,width)
midheight=int(height/2)
midwidth=int(width/2)

cv2.line(Image,(0,midheight),(width,midheight),(0,255,0),2)
cv2.line(Image,(midwidth,0),(midwidth,height),(0,255,0),2)
cv2.imshow("Image",Image)
    
