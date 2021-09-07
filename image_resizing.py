from PIL import Image
import numpy as np
import glob
import os

# 1. loading all images
filelist = glob.glob('images/colorized/smth_else/*.png')


# 2. resizing them accordingly - into 256x256!
new_size = (256, 256)

for infile in glob.glob("images/colorized/smth_else/*.png"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    # rgb_im = im.convert('RGB')
    new_im = im.resize((256, 256))
    print(new_im.size)


    file2 = file + '.png'
    new_im.save(file2)



# print(filelist)
X = np.array([np.array(Image.open(fname)) for fname in filelist])
print(X.shape)
print(type(X))


# image = Image.open('images/monalisa.jpg')
# # summarize some details about the image
# print(image.format)
# print(image.size)
# print(image.mode)
# # show the image
