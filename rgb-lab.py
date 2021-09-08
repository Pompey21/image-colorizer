from tensorflow.keras.preprocessing.image import load_img
from skimage.color import rgb2lab
from skimage.io import imshow

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = load_img('/Users/admin/Desktop/images/monalisa.jpg')
lab = rgb2lab(img)
L=lab[:,:,0]
A=lab[:,:,1]
B=lab[:,:,2]

# imshow(L, cmap='gray')

imgplot = plt.imshow(B,cmap='gray')
plt.show()