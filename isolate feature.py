import numpy as np
import cv2
Original=cv2.imread("Slide1.png")
Cannyimage=cv2.Canny(Original,150,250)
im2, cnts, hierarchy =cv2.findContours(Cannyimage,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
screenCnt=None
print (hierarchy)
cv2.imshow("Original",Original)
