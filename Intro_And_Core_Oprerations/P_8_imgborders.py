import numpy as py
import cv2 as cv
from matplotlib import pyplot as plt

# If you want to create a border around the image, something like a photo frame, you can use cv.copyMakeBorder(). 
# But it has more applications for convolution operation, zero padding etc. This function takes following arguments:
# 
#   src - input image
#   top, bottom, left, right - border width in number of pixels in corresponding directions
#   borderType - Flag defining what kind of border to be added. It can be following types:
#       cv.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
#       cv.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
#       cv.BORDER_REFLECT_101 or cv.BORDER_DEFAULT - Same as above, but with a slight change, like this : 
#               gfedcb|abcdefgh|gfedcba
#       cv.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
#       cv.BORDER_WRAP - Can't explain, it will look like this : cdefgh|abcdefgh|abcdefg
#   value - Color of border if border type is cv.BORDER_CONSTANT
#

BLUE = [ 255, 0, 0 ]

img1 = cv.imread("cars_P_8.jpg")

replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()
