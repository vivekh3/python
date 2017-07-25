##########################################################################################################################################
#This code is from the tutorial for Tensorflow - deep MNIST from experts. This line gives full credit to whoever wrote this. This is not my
#code. I have only attempted to put comments around the code for not-so-experts
###########################################################################################################################################

# This set of imports is to ensure that the code runs with older versions of Python.
# From the documentation : A future statement is a directive to the compiler that a particular module should be compiled using syntax or
# semantics that will be available in a specified future release of Python. The future statement is intended to ease migration to future
# versions of Python that introduce incompatible changes to the language. It allows use of the new features on a per-module basis before
# the release in which the feature becomes standard.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""
The Plan:
1. Import MNIST data
2. Define placeholders for x and y
3. Define variables W and b
4. Define functions to initialize weights and biases
5. Define convolution and max pooling functions, note the strides and padding for both
6. Initialize the weight and bias variables by calling the above functions
7. Apply the convolution and max pooling blocks - 2 in this case
8. Initiate a fully connected block by getting new values for W and b
9. Create a readout layer
10. 
    

"""


import sys
# These two lines below import the MNIST data set into mnist, note the use of one_hot. This means that the classification is a 10x10 array with 1 at
# the location of the output digit, e.g a number 2 is represented as [0 0 1 0 0 0 0 0 0 0] 
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
# importing tensorflow as tf
import tensorflow as tf

sess=tf.InteractiveSession()

#Placeholders, note that x, which is an image, is a 28x28 matrix, it has been 'flattened' to a 784 column row, similarly y_ is a 10 column matrix (one_hot)
x=tf.placeholder(tf.float32, shape=[None,784])
y_=tf.placeholder(tf.float32, shape=[None,10])

#initializing the weight and bias variables

W=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))

# The two functions below are used to pick initial randomly generated values for W and b. The values are picked from a normal distribution
# with a standard deviation of 0.1
def weight_variable(shape):
              initial = tf.truncated_normal(shape, stddev=0.1)
              return tf.Variable(initial)

def bias_variable(shape):
              initial = tf.constant(0.1,shape=shape)
              return tf.Variable(initial)
# This function conv2d does the convolution operation, note the parameters - x is the input layer, W is the weights, stride is 1 pixel, with a 1x1
# matrix, and there is no padding on the image (padding ='same'). Note the strides syntax - strides=[batch,height,width,depth]. Batch is related to
# the batch of images that is fed to the network, height and width are the dimensions of the sliding window, and depth is the number of filters, for a b&W
# image, the value is 1, whereas for an RGB image, the value is 3

def conv2d(x,W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')
#now we do a max_pooling operation. Essentially it finds the maximum value in a 2x2 window and pulls it out as the max pooled value, stride is also 2x2 here
# and there is no padding

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1, 2, 2, 1], padding='SAME')          

# initializing the weights, note that we are using a 5x5 window in the convolution step. The number of input channels is 1, and the kernel is 32 channels deep


W_conv1= weight_variable([5,5,1,32])
b_conv1=bias_variable([32])

# We are reshaping the image into a 4d tensor which is 28x28 in size with 1 channel

x_image=tf.reshape(x, [-1,28,28,1])

print (x)
