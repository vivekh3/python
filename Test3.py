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

plt.imshow(image,cmap='gray',extent=(1,32,32,64))
plt.axis('off')
str_comp_thinks="This is what the computer thinks this is: "
plt.text(-20,40,str_comp_thinks)
str_actual="This is what it actually is: "
plt.text(-20,45,str_actual)
plt.show()

