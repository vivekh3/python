from keras.models import load_model
from keras.datasets import cifar10
import matplotlib.pyplot as plt
import matplotlib.image as mpt
import os
import numpy as np
import cv2
import pickle

plt.rcParams['toolbar']='None'

# Setting up the path for the label names.
#You can uncomment it or use it if you like,
#I will just store the values in a static dictionary.
#The execution will be faster that way.
'''
path='C:\\Users\\vivek_hari\\.keras\\datasets\\cifar-10-batches-py\\'

def unpickle(file):  
    
    # Convert byte stream to object
    with open(path + file,'rb') as fo:
        print("Decoding file: %s" % (path+file))
        dict = pickle.load(fo, encoding='bytes')
       
    # Dictionary with images and labels
    return dict

def load_classes():
       raw = unpickle("batches.meta")[b'label_names']
       names = [x.decode('utf-8') for x in raw]
       return names
'''
# Loading the saved model    
#print (os.getcwd())
load_dir=os.path.join(os.getcwd(),'saved_models')
model=load_model(os.path.join(load_dir,'keras_cifar10_trained_model.h5'))
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
# Run this test for 5 iterations
#setting up the dpi level for calculating the plot
dpi=100
mleft=300
mright=300
mtop=30
mbottom=200

for p in range(0,5):

# Picking up a random image
    i=np.random.randint(1,10000)
    # Printing the index of the image from the 10K samples
    print (i)
    mpt.imsave("Test.jpg",x_test[i])
    
    image=mpt.imread("Test.jpg")
    figwidth= (image.shape[1]+mleft+mright)/float(dpi)
    figheight = (image.shape[0]+mtop+mbottom)/float(dpi)

    fig=plt.figure(figsize=(figwidth,figheight))
    fig.subplots_adjust(left=mleft/float(dpi)/figwidth,
                    right=1.-mright/float(dpi)/figwidth,
                    top=1.-mtop/float(dpi)/figheight,
                    bottom=mbottom/float(dpi)/figheight)
    plt.imshow(image,cmap='gray')
    plt.axis('off')
    
# Now Keras.predict expects the input to be a 4D tensor.
# But our image is a 3D tensor of the shape(32,32,3).
# We will augment the input matrix by adding one more dimension

    y=np.expand_dims(x_test[i],axis=0)

# Now the predictions

    predictions=model.predict(y)
# Check which element of the predictions matrix is the highest.
#This gives you the class with the highest probability

    check=np.argmax(predictions)
#Here we get the class names, uncomment this next line and comment the next line
#in case you plan to use the class names loading functions commented above

#class_names=load_classes()
    class_names=['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
# Printing the class names, uncomment the line below if needed
#    print (class_names)
# And now the actual test
    str_comp_thinks="This is what the computer thinks this is: " + str(class_names[check])
    plt.text(0.1,50,str_comp_thinks, ha="center")
    str_actual="This is what it actually is: "+ class_names[np.asscalar(y_test[i])]
    plt.text(5,80,str_actual,ha="center")
    #print("This is what the computer thinks this is: " + class_names[check])
# Validating the test
   # print("This is what it actually is: "+ class_names[np.asscalar(y_test[i])])
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

