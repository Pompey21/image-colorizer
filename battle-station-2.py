from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from tensorflow.keras.layers import Conv2D, UpSampling2D
from PIL import Image
from tensorflow.keras.models import Sequential
from skimage.color import rgb2lab
import numpy as np
import glob

# loading all images
filelist = glob.glob('/Users/admin/Desktop/images/colorized/smth_else/*.png')

# reading images into a numpy array
X = np.array([np.array(Image.open(fname)) for fname in filelist])
print(X.shape)
print(type(X))

print("----------------------------")
print(X[0])

# normalise every pixel -> need to divide it by 255
X_normalised = np.array([img/255 for img in X])


print("----------------------------")
print("---------||||||||||---------")
print("---------^^^^^^^^^^---------")
print("----------------------------")
print(X_normalised[0])



"""
	All images need to be converted from a RGB to LAB compontents
	->
	by iterating on each image, we convert the RGB to LAB.
	Think of LAB image as a grey image in L channel and all color info stored in A and B channels.
	The input to the network will be the L channel, so we assign L channel to X vector.
	And assign A and B to Y.

"""

X =[]
Y =[]
for img in X_normalised:
      lab = rgb2lab(img)
      X.append(lab[:,:,0])
      Y.append(lab[:,:,1:] / 128) #A and B values range from -127 to 128,
      #so we divide the values by 128 to restrict values to between -1 and 1.

X = np.array(X)
Y = np.array(Y)
X = X.reshape(X.shape+(1,)) #dimensions to be the same for X and Y
print(X.shape)
print(Y.shape)



# ==============================================================================
# ==============================================================================
#Encoder

model = Sequential()
model.add(Conv2D(64, (3, 3), activation='relu', padding='same', strides=2, input_shape=(256, 256, 1)))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(128, (3,3), activation='relu', padding='same', strides=2))
model.add(Conv2D(256, (3,3), activation='relu', padding='same'))
model.add(Conv2D(256, (3,3), activation='relu', padding='same', strides=2))
model.add(Conv2D(512, (3,3), activation='relu', padding='same'))
model.add(Conv2D(512, (3,3), activation='relu', padding='same'))
model.add(Conv2D(256, (3,3), activation='relu', padding='same'))

#Decoder
#Note: For the last layer we use tanh instead of Relu.
#This is because we are colorizing the image in this layer using 2 filters, A and B.
#A and B values range between -1 and 1 so tanh (or hyperbolic tangent) is used
#as it also has the range between -1 and 1.
#Other functions go from 0 to 1.
model.add(Conv2D(128, (3,3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(64, (3,3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(32, (3,3), activation='relu', padding='same'))
model.add(Conv2D(16, (3,3), activation='relu', padding='same'))
model.add(Conv2D(2, (3, 3), activation='tanh', padding='same'))
model.add(UpSampling2D((2, 2)))
model.compile(optimizer='adam', loss='mse' , metrics=['accuracy'])
model.summary()


model.fit(X,Y,validation_split=0.1, epochs=5, batch_size=16)

model.save('other_files/colorize_autoencoder.model')









