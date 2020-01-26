import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)
time.sleep(5)

if cap.isOpened() == False:
    print ("Problem Accessing the camera")

    
while(True):
    # Capture frame-by-frame
    ret, frames = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frames',frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
