import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

##########
# Image Gradient or Edge Detection
# --------------------------------
#
# OpenCV provides three types of gradient filters or High-pass filters, Sobel, Scharr 
# and Laplacian. 
#
# 1. Sobel and Scharr Derivatives
# -------------------------------
# Sobel operators is a joint Gausssian smoothing plus differentiation operation, so it is more 
# resistant to noise. You can specify the direction of derivatives to be taken, vertical or horizontal 
# (by the arguments, yorder and xorder respectively). You can also specify the size of kernel by the argument ksize.
# If ksize = -1, a 3x3 Scharr filter is used which gives better results than 3x3 Sobel filter.
#
#
# 2. Laplacian Derivatives
# ------------------------
# It calculates the Laplacian of the image given by the relation, 
#           Δsrc= ∂2src/∂x2 + ∂2src/∂y2 
# where each derivative is found using Sobel derivatives. 
# If ksize = 1, then following kernel is used for filtering:
#
#                 __     __
#                |         |
#                | 0  1  0 |
#       kernel = | 1 -4  1 |
#                | 0  1  0 |
#                |__     __|
#

img = cv.imread("../resources/sudoku.jpg")

img = cv.cvtColor( img, cv.COLOR_BGR2GRAY )
img = cv.GaussianBlur( img, (5,5), 0 )

#th = cv.adaptiveThreshold( img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2 )
#
#kernel = np.ones( (5,5), np.uint8 )
#opening = cv.morphologyEx( th, cv.MORPH_OPEN, kernel )

laplacian = cv.Laplacian( img, cv.CV_64F )
sobelx = cv.Sobel( img, cv.CV_64F, 1, 0, ksize = 5 )
sobely = cv.Sobel( img, cv.CV_64F, 0, 1, ksize = 5 )

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian, cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()

