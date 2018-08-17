import numpy as np
import cv2 as cv

img = cv.imread( "cars.jpg" )


##########
# Scaling is just resizing of the image. OpenCV comes with a function cv.resize() for this purpose. 
# The size of the image can be specified manually, or you can specify the scaling factor. 
# Different interpolation methods are used. Preferable interpolation methods are cv.INTER_AREA for 
# shrinking and cv.INTER_CUBIC (slow) & cv.INTER_LINEAR for zooming. By default, interpolation 
# method used is cv.INTER_LINEAR for all resizing purposes. You can resize an input image either of following methods


res = cv.resize( img, None, fx = 2, fy = 2, interpolation = cv.INTER_CUBIC )

cv.imshow( "First Method", res )

# OR

height, width = img.shape[:2]
res = cv.resize( img, ( 2*width, 2*height ), interpolation = cv.INTER_CUBIC )

cv.imshow( "Second Method", res )
cv.waitKey(0)
cv.destroyAllWindows()
