import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


##########
# In the previous section, we used a global value as threshold value. But it may not be
# good in all the conditions where image has different lighting conditions in 
# different areas. In that case, we go for adaptive thresholding. In this, the algorithm
# calculate the threshold for a small regions of the image. So we get different 
# thresholds for different regions of the same image and it gives us better results
# for images with varying illumination.
#
# It has three ‘special’ input params and only one output argument.
#
# - Adaptive Method - It decides how thresholding value is calculated.
#       cv.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
#       cv.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood 
#               values where weights are a gaussian window.
#
# - Block Size - It decides the size of neighbourhood area.
# - C - It is just a constant which is subtracted from the mean or weighted mean calculated.
#
# Below piece of code compares global thresholding and adaptive thresholding for an image with varying illumination.
#


img = cv.imread( "../resources/sudoku.jpg", 0 )

# Blurs an image using the median filter.
# The function smoothes an image using the median filter with the ksize×ksize aperture. 
# Each channel of a multi-channel image is processed independently. In-place operation is supported.
# ksize is the second arg
img = cv.medianBlur( img, 5 )

ret, th1 = cv.threshold( img, 127, 255, cv.THRESH_BINARY )
th2 = cv.adaptiveThreshold( img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2 )
th3 = cv.adaptiveThreshold( img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2 )

titles = [ "Original Image", "Global Thresholding ( v = 127 )", 
        "Adaptive Mean Thresholding", "Adaptive Guassian Thresholding" ]

images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()




















