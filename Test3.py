import matplotlib.pyplot as plt
import matplotlib.image as mpt
import numpy as np
image=plt.imread("Test.jpg")
height,width,depth=image.shape
figsize=5,5
fig=plt.figure(figsize=figsize)
plt.show()
