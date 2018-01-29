import matplotlib.pyplot as plt
import matplotlib.image as mpt
import numpy as np
#fig, ax = plt.subplots()
#plt.subplot(211)
plt.subplot(211)
image = plt.imread("Test.jpg")
dpi=80

height, width, depth = image.shape
figsize = (width) / float(dpi), (height) / float(dpi)
fig=plt.figure(figsize=figsize)

#ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
#ax.axis('off')

    # Display the image.
#ax.subplot(211)

plt.axis('off')

implot=plt.imshow(image, cmap='gray')

'''
w,h,d=32,32,4
A = np.fromstring(image, np.uint16).astype(float).reshape((w, h,d))
A /= A.max()

dpi=80

fig, ax = plt.subplots()
extent = (0, 32, 0, 32)
im = ax.imshow(image, cmap=plt.cm.hot, origin='upper', extent=extent)
'''
plt.show()
