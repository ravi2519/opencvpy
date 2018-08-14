import numpy as py
import cv2 as cv

img_clr = cv.imread( "cars.jpg" )
img_gry = cv.imread( "cars_gray.jpg" )

##########
# The shape of an image is accessed by img.shape. It returns a tuple of number of rows, 
# columns, and channels (if image is color)
#
# If an image is grayscale, the tuple returned contains only the number of rows and columns, 
# so it is a good method to check whether the loaded image is grayscale or color.
#

print ( "Color image shape is " + str( img_clr.shape ) )
print ( "Gray image shape is " + str( img_gry.shape ) )

##########
# Total number of pixels is accessed by img.size

print ( "Image number of pixels are " + str ( img_clr.size ) )

##########
# Image datatype is obtained by `img.dtype`

print ( "Image datatype is " + str( img_clr.dtype ) )
