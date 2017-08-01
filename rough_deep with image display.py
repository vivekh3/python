###########################################################################################################################################
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
import numpy as np
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
import cv2

sess=tf.InteractiveSession()

#Placeholders, note that x, which is an image, is a 28x28 matrix, it has been 'flattened' to a 784 column row, similarly y_ is a 10 column matrix (one_hot)
x=tf.placeholder(tf.float32, shape=[None,784])
y_=tf.placeholder(tf.float32, shape=[None,10])
x_test=tf.placeholder(tf.float32, shape=[None,784])
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

# The first convolution operation is as below, we are convoluting the input, and then applying a relu activation function, here we are not using sigmoid as an
# function.

h_conv1=tf.nn.relu(conv2d(x_image,W_conv1)+b_conv1)
h_pool1=max_pool_2x2(h_conv1)

# Applying the second convolution layer, note that we are getting 32 channels as an output from the first convolution layer and we are getting 64 channels as an output
# Also note that a 2x2 max pooling reduces the size of the image from a 28x28 to 14x14, and the second convolution operation reduces the size from 14x14 to 7x7

W_conv2= weight_variable([5,5,32,64])
b_conv2=bias_variable([64])

h_conv2=tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2)
h_pool2=max_pool_2x2(h_conv2)

# Now for the fully connected layer, remember the size of the input image is 7x7x64 channels from the second convolution layer, and we are pushing it to 1024 channels


W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
# Reshaping the output

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# Dropout, this randomly drops neurons in the process, more on this later, but this tends to reduce overfitting of the network.

keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# Readout
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2


# now for the reduction of the cross entropy using the adam optimizer

cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))

train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# This finds out how many times the predicted value from the network was equal to the actual value

correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Initiate the tf session
sess.run(tf.global_variables_initializer())

# And the iterations..! Note that the system is printing the training accuracy after every 100 cycles, and is taking 50 images in one batch
# the system then finally prints out the test accuracy at the end. Another thing to note is the 

for i in range(200):
  batch = mnist.train.next_batch(50)
  if i%20 == 0:
    train_accuracy = accuracy.eval(feed_dict={
        x:batch[0], y_: batch[1], keep_prob: 1.0})
    print("step %d, training accuracy %g"%(i, train_accuracy))
  train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

print("test accuracy %g"%accuracy.eval(feed_dict={
    x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))


with sess.as_default():
    for i in range(1,10):
        x_test=mnist.test.images[i]
        x_test=np.reshape(x_test,(-1,784))
      
        k=y_conv.eval(feed_dict={x:x_test,keep_prob:1})
        d=tf.nn.softmax(k,dim=-1)
        print(sess.run(d,feed_dict={y_conv:k}))
        print("This is what the machine sees")
        print(sess.run(tf.round(sess.run(d,feed_dict={y_conv:k}))))
        print("This is what it is actually")
        print(mnist.test.labels[i])
        image_check=np.array(x_test,dtype='float32')
        image_check=image_check.reshape((28,28))
        cv2.imshow('check',image_check)
        print ("This is a: %d"%sess.run(tf.arg_max(tf.round(sess.run(d,feed_dict={y_conv:k})),1)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
   # print (accuracy.eval(feed_dict={x: np.reshape(mnist.test.images[11],(-1,784)), y_: np.reshape(mnist.test.labels[10],(-1,10)), keep_prob: 1.0}))
    


