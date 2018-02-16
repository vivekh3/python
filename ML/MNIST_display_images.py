import tensorflow as tf
import cv2
import numpy as np
from msvcrt import getch
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

for i in range(1,100):
    input("Please press a key to continue..")
        
    image_check = mnist.test.images[i]
    label_check = mnist.test.labels[i]
    print (label_check)
    image_check=np.array(image_check,dtype='float32')
    image_check=image_check.reshape((28,28))
    cv2.imshow('check',image_check)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
