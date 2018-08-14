import numpy as np
import cv2 as cv

img = cv.imread( "cars.jpg" )

##########
# You can add two images by OpenCV function, cv.add() or simply by numpy operation, 
# res = img1 + img2. Both images should be of same depth and type, 
# or second image can just be a scalar value.
#
# There is a difference between OpenCV addition and Numpy addition. 
# OpenCV addition is a saturated operation while Numpy addition is a modulo operation.

x = np.uint8( [250] )
y = np.uint8( [10] )

print ( "OpenCV additon is " + str( cv.add( x, y ) ) ) # 250+10 = 260 => 255

print ( "Numpy addition is " + str ( x + y ) ) # 250+10 = 260 % 256 = 4
