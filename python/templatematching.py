import numpy as np
import cv2
img=cv2.imread( "slide1.jpg")
cv2.imshow('Image',img)
cannyimg=cv2.Canny(img,100,200)
cv2.imshow('Canny',cannyimg)
      im2, cnts, hierarchy =cv2.findContours(cannyimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
      cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
      screenCnt=None
      for c in cnts:
            epsilon=0.02*cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,epsilon,True)
            print (approx)
            if len(approx)==4:
               screenCnt=approx
               break       
      final=cv2.drawContours(img,[screenCnt],-1,(0,255,0),15)
      cv2.imshow("Contours", final)
      cv2.waitKey(0)
