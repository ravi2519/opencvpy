import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

##########
# Canny Edge Detection
# --------------------
# It is a multistage algorithm:
# 1. Noise Reduction: Gaussin filter of 5x5 kernel is applied to reduce the noise.
# 2. Finding Intensity Gradient of the Image : An edge in an image may point in a 
#    variety of directions, so the Canny algorithm uses four filters to detect horizontal, 
#    vertical and diagonal edges in the blurred image. The edge detection operator Sobel
#    returns a value of first derivative in the horizontal direction ( Gx ) and vertical
#    direction ( Gy ). From this the edge gradient and direction is determined.
# 3. Non-maximum Suppression : After getting gradient magnitude and direction, a full scan 
#    of image is done to remove any unwanted pixels which may not constitute the edge. 
#    For this, at every pixel, pixel is checked if it is a local maximum in its neighborhood 
#    in the direction of gradient. This way the gradient edge before can be thinned.
# 4. Double Threshold: After application of non-maximum suppression, remaining edge pixels 
#    provide a more accurate representation of real edges in an image. However, some edge pixels 
#    remain that are caused by noise and color variation. In order to account for these spurious 
#    responses, it is essential to filter out edge pixels with a weak gradient value and
#    preserve edge pixels with a high gradient value. This is accomplished by selecting high
#    and low threshold values. If an edge pixel’s gradient value is higher than the high threshold 
#    value, it is marked as a strong edge pixel. If an edge pixel’s gradient value is smaller
#    than the high threshold value and larger than the low threshold value, it is marked as a 
#    weak edge pixel. If an edge pixel's value is smaller than the low threshold value, it will i
#    be suppressed. 
# 5. Hysteresis Thresholding : Weak edges are removed in this step
# 
# OpenCV puts all the above in single function, cv.Canny(). We will see how to use it. First argument is our input image. Second and third arguments are our minVal and maxVal respectively. Third argument is aperture_size. It is the size of Sobel kernel used for find image gradients. By default it is 3. Last argument is L2gradient which specifies the equation for finding gradient magnitude. If it is True, it uses the equation mentioned above which is more accurate, otherwise it uses this function: Edge_Gradient(G)=|Gx|+|Gy|. By default, it is False.

img = cv.imread( "../resources/messi5.jpg", 0 )

edges = cv.Canny( img, 100, 200 )

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
