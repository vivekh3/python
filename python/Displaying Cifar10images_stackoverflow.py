import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['toolbar']='None'
image=np.random.rand(32,32)
dpi = 100

mleft = 100  # pixel
mright = 100 #
mtop= 30 
mbottom=200

figwidth= (image.shape[1]+mleft+mright)/float(dpi)
figheight = (image.shape[0]+mtop+mbottom)/float(dpi)

fig=plt.figure(figsize=(figwidth,figheight))
fig.subplots_adjust(left=mleft/float(dpi)/figwidth,
                    right=1.-mright/float(dpi)/figwidth,
                    top=1.-mtop/float(dpi)/figheight,
                    bottom=mbottom/float(dpi)/figheight)

plt.imshow(image,cmap='gray')
plt.axis('off')
str_comp_thinks="Text1"
fig.text(0.5,0.3,str_comp_thinks, ha="center")
str_actual="Text2"
fig.text(0.5,0.1,str_actual, ha="center")
plt.show()
