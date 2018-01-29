import matplotlib.pyplot as plt
import matplotlib.image as mpt
import numpy as np
plt.rcParams['toolbar']='None'
image=mpt.imread('Avnet.jpg')
imgplot=plt.imshow(image)
plt.text(50,100,"This is what the computer thinks this is: "+"hello")
plt.xlabel("Here it is")
plt.axis('off')

def display_image_in_actual_size(im_path):

    dpi = 80
    im_data = plt.imread(im_path)
    height, width, depth = im_data.shape

    # What size does the figure need to be in inches to fit the image?
    figsize = (width) / float(dpi), (height) / float(dpi)
    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

plt.subplot(211)
dpi = 80
im_data = plt.imread("Test.jpg")
height, width, depth = im_data.shape
figsize = (width) / float(dpi), (height) / float(dpi)
fig = plt.figure(figsize=figsize)
ax = fig.add_axes([0, 0, 1, 1])
# Hide spines, ticks, etc.
ax.axis('off')
abc=plt.imshow(im_data, cmap='gray')
#display_image_in_actual_size("Test.jpg")
#dpi=90
#im_data=mpt.imread("Test.jpg")
#height, width, depth = im_data.shape
#figsize = (width) / float(dpi), (height) / float(dpi)
#fig = plt.figure(figsize=figsize)
#ax = fig.add_axes([0, 0, 1, 1])
#plt.axis('Off')

#im_plot=plt.imshow(im_data, cmap='gray')
plt.show()
