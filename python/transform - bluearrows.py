import numpy as np
import cv2

cap=cv2.VideoCapture(0)
Original=cv2.imread("Arrows\Slide2.jpg")
#cv2.imshow("original",Original)
#cv2.namedWindow('Trackers')
#def nothing(x):
 #   pass
#cv2.createTrackbar('LG','Trackers',0,500,nothing)
#cv2.createTrackbar('UG','Trackers',0,500,nothing)

while (True):
      ret,Image=cap.read()
      #LG=cv2.getTrackbarPos('LG','Trackers')
      #UG=cv2.getTrackbarPos('UG','Trackers')

      Cannyimage=cv2.Canny(Image,176,276)
      cv2.imshow("Canny",Cannyimage)
      im2, cnts, hierarchy =cv2.findContours(Cannyimage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
      cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
      screenCnt=None

      for c in cnts:
     
            epsilon=0.05*cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,epsilon,True)
            #print (approx)
            #print (c)
            if len(approx)==4:
                 screenCnt=approx
            break
      print (screenCnt)
      #pts=cv2.Reshape(screenCnt,4,2)
      rectpoints=np.zeros((4,2),dtype="float32")
      s=screenCnt.sum(axis=1)
      rectpoints[0]=screenCnt[np.argmin(s)]
      rectpoints[2]=screenCnt[np.argmax(s)]

      #diff=np.diff(pts,axis=1)
      #rectpoints[1]=pts[np.argmin(diff)]
      #rectpoints[3]=pts[np.argmax(diff)]
      #print (rectpoints)
     # (tl,tr,bl,br)=rectpoints

      x,y,w,h=cv2.boundingRect(screenCnt)
      print (x,y,w,h)

      Rect=cv2.rectangle(Image.copy(),(x,y),(x+w,y+h),(0,255,0),2)
      cv2.imshow("Rectangle",Rect)
#final=cv2.drawContours(Image,[screenCnt],-1,(0,255,0),3)
#dst=np.array([[x,y],[x+w,y],[x+w,y+h],[x,y+h]], dtype="float32")

#M=cv2.getPerspectiveTransform(rectpoints,dst)
#final=cv2.warpPerspective(Image.copy(),M,(1280,720))
#cv2.imshow("Contours", final)
#cropped=final[y:y+h,x:x+w]
#cv2.imshow("Cropped",cropped)
#refmat=np.array([[0,0],[1280,0],[1280,720],[0,720]], dtype="float32")
#print ("dst",dst)
#print ("refmat",refmat)
#M2=cv2.getPerspectiveTransform(dst,refmat)
#print ("M2",M2)
#final2=cv2.warpPerspective(final.copy(),M2,(1280,720))
#cv2.imshow("FINAL",final2)
#cv2.imshow("Original",Original)
# bitwise xor
#res=cv2.bitwise_xor(final2,Original)
#cv2.imshow("result",res)
      k=cv2.waitKey(1)
      if k==27:
           break

    
cv2.destroyAllWindows()
cap.release()
