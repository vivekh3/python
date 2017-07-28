import cv2
import numpy as np
import csv

with open('mnist_test.csv','r') as csv_file:
    for data in csv.reader (csv_file):
        label=data[0]
        pixels = data[1:]
        pixels=np.array(pixels,dtype='uint8')
        pixels=pixels.reshape(28,28)
        title='Label is {label}'.format(label=label)
        cv2.imshow(title,pixels)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


        
        
