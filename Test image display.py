import numpy as np
import cv2
import time
cv2.namedWindow("Test",cv2.WINDOW_AUTOSIZE)
cv2.resizeWindow("Test",500,500)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText("Test","This text here",(10,10),font,1.0,(0, 255, 0), 2)
'''
original=cv2.imread("Avnet.jpg")
cv2.imshow("Test",original)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(original,"This text here",(10,10),font,1.0,(0, 255, 0), 2)
#time.sleep(1)
#cv2.destroyAllWindows()

'''
