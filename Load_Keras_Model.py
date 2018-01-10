from keras.models import load_model
from keras.datasets import cifar10
import os
import numpy as np
import opencv as cv2


print (os.getcwd())
#load_dir=os.path.join(os.getcwd(),'saved_models')
#model=load_model(os.path.join(load_dir,'keras_cifar10_trained_model.h5'))
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print(x_test.shape[0],'Test Samples')
x_test_2=np.reshape(x_test[1],(-1,1024))
image_check=np.array(x_test_2,dtype='float32')
image_check=image_check.reshape((32,32,3))
cv2.imshow('test',image_check)





