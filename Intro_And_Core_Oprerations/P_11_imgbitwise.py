import numpy as py
import cv2 as cv

##########
# Bitwise Operations
# This includes bitwise AND, OR, NOT and XOR operations. 
# They will be highly useful while extracting any part of the image 
# (as we will see in coming chapters), defining and working with non-rectangular ROI etc. 
# Below we will see an example on how to change a particular region of an image.
#
# I want to put OpenCV logo above an image. If I add two images, it will change color. 
# If I blend it, I get an transparent effect. But I want it to be opaque. 
# If it was a rectangular region, I could use ROI as we did in last chapter. 
# But OpenCV logo is a not a rectangular shape. So you can do it with bitwise operations as below
#

# load two images
img1 = cv.imread("cars.jpg")
img2 = cv.imread("opencv_logo.png")

# logo needs to be placed on top left, so i create a ROI
rows, cols, channels = img2.shape
roi = img1[ 0:rows, 0:cols ] # ROI will be equal to the rows and cols of logo on the image

# create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor( img2, cv.COLOR_BGR2GRAY ) # cvtColor is used to convert the color space of the image
                                                  # https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html#ga397ae87e1288a81d2363b61574eb8cab
ret, mask = cv.threshold( img2gray, 10, 255, cv.THRESH_BINARY ) # The function is typically used to get a bi-level (binary) 
                                                                # image out of a grayscale image or for removing a noise, that
                                                                # is, filtering out pixels with too small or too large values. 
                                                                # https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57
cv.imshow( "Mask", mask )
cv.waitKey(0)
cv.destroyAllWindows()

mask_inv = cv.bitwise_not( mask )
cv.imshow( "Inverse Mask", mask_inv )
cv.waitKey(0)
cv.destroyAllWindows()

# now black out the area of logo in ROI
img1_bg = cv.bitwise_and( roi, roi, mask = mask_inv )
cv.imshow( "Blackout area for logo on ROI", img1_bg )
cv.waitKey(0)
cv.destroyAllWindows()

# take only region of logo from logo images
img2_fg = cv.bitwise_and( img2, img2, mask = mask )
cv.imshow( "Masked logo ing", img2_fg )
cv.waitKey(0)
cv.destroyAllWindows()

# put logo in ROI and modify the main image
dst = cv.add( img1_bg, img2_fg )
cv.imshow( "dst", dst )
cv.waitKey(0)
cv.destroyAllWindows()

img1[0:rows, 0:cols] = dst

cv.imshow( "res", img1 )
cv.waitKey(0)
cv.destroyAllWindows()
