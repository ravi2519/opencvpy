import numpy as np
import cv2 as cv

##########
#
# Rotation of an image for an angle θ is achieved by the transformation matrix of the form
# 
#            __         __
#           |             |
#           | cosθ -sinθ  |
#       M = |             |
#           | sinθ cosθ   |
#           |__         __|
#
#       
# But OpenCV provides scaled rotation with adjustable center of rotation so that you can rotate 
# at any location you prefer. Modified transformation matrix is given by
#
#            __                                     __
#           |                                         |
#           | α     β       (1−α)⋅center.x−β⋅center.y |
#       M = |                                         |
#           | -β    α       β⋅center.x+(1−α)⋅center.y |
#           |__                                     __|
#
#
# where:
#
#       α=scale⋅cosθ,
#       β=scale⋅sinθ
#
# To find this transformation matrix, OpenCV provides a function, cv.getRotationMatrix2D. 
#   retval	=	cv.getRotationMatrix2D(	center, angle, scale	)
#
# Check below example which rotates the image by 90 degree with respect to center without any scaling.
#

img = cv.imread( "cars.jpg", 0 )
rows,cols = img.shape

# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D( ( ( cols - 1 )/2.0, ( rows - 1 )/2.0 ), 90, 1 )
dst = cv.warpAffine( img, M, ( cols, rows ) )

cv.imshow( "Rotation", dst )
cv.waitKey(0)
cv.destroyAllWindows()


