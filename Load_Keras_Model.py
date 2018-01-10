from keras.models import load_model
from keras.datasets import cifar10
import os
import numpy as np
import cv2


print (os.getcwd())
load_dir=os.path.join(os.getcwd(),'saved_models')
model=load_model(os.path.join(load_dir,'keras_cifar10_trained_model.h5'))
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

i=np.random.randint(1,10000)
print (i)
print(x_test.shape[0],'Test Samples')
print(x_test[i].shape)
cv2.imshow('Image 1',x_test[i])



