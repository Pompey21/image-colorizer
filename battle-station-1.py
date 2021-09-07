from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from PIL import Image
import numpy as np
import glob


###################################################################
# This is old way of reading images!!
###################################################################
# # loading all images
# filelist = glob.glob('images/colorized/smth_else/*.png')

# # reading images into a numpy array
# X = np.array([np.array(Image.open(fname)) for fname in filelist])
# print(X.shape)
# print(type(X))
###################################################################


""" 
	Data Preparation - defined the path to the image database and 
	then read them using the two functions for rescaling!
"""

path = "images/colorized/"

# data pre-processing -> making sure it is normalised
train_datagen = ImageDataGenerator(rescale=1. / 255)

# resize images, if needed
train = train_datagen.flow_from_directory(path,
                                          target_size=(256, 256),
                                          batch_size=1,
                                          class_mode=None)


"""
	All images need to be converted from a RGB to LAB compontents
"""
"""
by iterating on each image, we convert the RGB to LAB.
Think of LAB image as a grey image in L channel and all color info stored in A and B channels.
The input to the network will be the L channel, so we assign L channel to X vector.
And assign A and B to Y.

"""

X =[]
Y =[]
for img in train[0]:
  try:
      lab = rgb2lab(img)
#       X.append(lab[:,:,0])
#       Y.append(lab[:,:,1:] / 128) #A and B values range from -127 to 128,
#       #so we divide the values by 128 to restrict values to between -1 and 1.
  except:
     print('error')
# X = np.array(X)
# Y = np.array(Y)
# X = X.reshape(X.shape+(1,)) #dimensions to be the same for X and Y









