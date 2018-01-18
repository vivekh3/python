import matplotlib.pyplot as plt
import matplotlib.image as mpt
import numpy as np
plt.rcParams['toolbar']='None'
image=mpt.imread('Avnet.jpg')
imgplot=plt.imshow(image)
plt.text(50,100,"This is what the computer thinks this is: "+"hello")
plt.xlabel("Here it is")
plt.axis('off')
plt.show()
