import numpy as np
import cv2 as cv

##########
# This is also image addition, but different weights are given to images so that it 
# gives a feeling of blending or transparency. Images are added as per the equation below:
#
#               g(x)=(1−α)f0(x)+αf1(x)
# By varying α from 0→1, you can perform a cool transition between one image to another.
#
# Here I took two images to blend them together. First image is given a weight of 0.7 
# and second image is given 0.3. cv.addWeighted() applies following equation on the image.
#
#               dst=α⋅img1+β⋅img2+γ
# Here γ is taken as zero.

img1 = cv.imread( "cars.jpg" )
img2 = cv.imread( "costly_car.jpg" )

dst = cv.addWeighted( img1, 0.7, img2, 0.3, 0 )

cv.imshow( "dst", dst )
cv.waitKey(0)
cv.destroyAllWindows()

