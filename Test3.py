import matplotlib.pyplot as plt
import matplotlib.image as mpt
import numpy as np
from PIL import Image
plt.rcParams['toolbar']='None'
image=plt.imread("Test.jpg")
height,width,depth=image.shape
figsize=350/80,300/80
fig=plt.figure(figsize=figsize)
plt.plot([1,2,3])
plt.subplot(211)
first_image = np.array(image, dtype='float')
pixels = first_image.reshape((32, 32,-1))
plt.imshow(pixels, cmap='gray')
#plt.imshow(image,cmap='gray',interpolation='none', extent=(0,32,32,64))
plt.axis('off')
str_comp_thinks="This is what the computer thinks this is: "
plt.text(-20,20,str_comp_thinks)
str_actual="This is what it actually is: "
plt.text(-20,25,str_actual)
plt.show()

