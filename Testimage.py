import cv2
import numpy as np

image=cv2.imread('Avnet.jpg')

im2=cv2.line(image,(0,0),(10,10),(0,0,255),3)
cv2.imshow('Test',im2)
