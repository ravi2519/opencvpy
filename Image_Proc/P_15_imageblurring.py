import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

##########
# Image Blurring (Image Smoothing)
# --------------------------------
# Image blurring is achieved by convolving the image with a low-pass filter kernel. 
# It is useful for removing noises. It actually removes high frequency content 
# (eg: noise, edges) from the image. So edges are blurred a little bit in this operation.
# (Well, there are blurring techniques which doesn't blur the edges too). OpenCV provides 
# mainly four types of blurring techniques.
#
#
# 1. Averaging
# ------------
# This is done by convolving image with a normalized box filter. It simply takes the average
# of all the pixels under kernel area and replace the central element. This is done by the 
# function cv.blur() or cv.boxFilter(). Check the docs for more details about the kernel. 
# We should specify the width and height of kernel. A 3x3 normalized box filter would look like below:
#
#                     __       __
#                    |           |
#                    | 1   1   1 |
#                1   |           |
#           K = ---- | 1   1   1 |
#                9   |           |
#                    | 1   1   1 |
#                    |__       __|
#
#

img = cv.imread( "../resources/opencv_logo.png" )

blur =  cv.blur( img, (5,5) )

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#
# 2. Gaussian Blurring
# --------------------
# In this, instead of box filter, gaussian kernel is used. It is done with the function, 
# cv.GaussianBlur(). We should specify the width and height of kernel which should be 
# positive and odd. We also should specify the standard deviation in X and Y direction, 
# sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as same as 
# sigmaX. If both are given as zeros, they are calculated from kernel size. Gaussian blurring 
# is highly effective in removing gaussian noise from the image.
# 
# If you want, you can create a Gaussian kernel with the function, cv.getGaussianKernel().
# 
# The above code can be modified for Gaussian blurring:
#

gaussianblur = cv.GaussianBlur( img, (5,5), 0 )

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(gaussianblur),plt.title('Gaussian Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

# 
# 3. Median Blurring
# ------------------
# Here, the function cv.medianBlur() takes median of all the pixels under kernel area and 
# central element is replaced with this median value. This is highly effective against 
# salt-and-pepper noise in the images. Interesting thing is that, in the above filters, 
# central element is a newly calculated value which may be a pixel value in the image or a 
# new value. But in median blurring, central element is always replaced by some pixel value 
# in the image. It reduces the noise effectively. Its kernel size should be a positive odd integer.
#

#noiseimg = cv.imread( "../resources/noise5.jpg" )

median = cv.medianBlur( img, 5 )

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Median Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


# 4. Bilateral Filtering
# ----------------------
# cv.bilateralFilter() is highly effective in noise removal while keeping edges sharp. 
# But the operation is slower compared to other filters. We already saw that gaussian filter 
# takes the a neighbourhood around the pixel and find its gaussian weighted average. This gaussian 
# filter is a function of space alone, that is, nearby pixels are considered while filtering. 
# It doesn't consider whether pixels have almost same intensity. It doesn't consider whether 
# pixel is an edge pixel or not. So it blurs the edges also, which we don't want to do.
# 
# Bilateral filter also takes a gaussian filter in space, but one more gaussian filter which is a 
# function of pixel difference. Gaussian function of space make sure only nearby pixels are considered 
# for blurring while gaussian function of intensity difference make sure only those pixels with 
# similar intensity to central pixel is considered for blurring. So it preserves the edges since 
# pixels at edges will have large intensity variation.
# 
bilatblur = cv.bilateralFilter( img, 9, 75, 75 )

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(bilatblur),plt.title('bilateral Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
