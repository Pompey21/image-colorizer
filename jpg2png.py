from PIL import Image
import os

os.chdir('/Users/admin/Desktop/images/colorized/smth_else/')
list_img = os.listdir('/Users/admin/Desktop/images/colorized/smth_else/')

# PNG to JPG
for img in list_img:
	strss = '/Users/admin/Desktop/images/colorized/smth_else/' + img
	print(strss[:-3])
	strss_jpg = strss[:-3] + 'png'
	print(strss_jpg)
	os.rename(strss, strss_jpg)
	