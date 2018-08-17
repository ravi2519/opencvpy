import numpy as np
import cv2 as cv

##########
#
# Translation is the shifting of object's location. If you know the shift in (x,y) direction, 
# let it be (tx,ty), you can create the transformation matrix M as follows:
#            __    __
#           |        |
#           | 1 0 tx |
#       M = |        |
#           | 0 1 ty |
#           |__    __|
#
#       
# You can take make it into a Numpy array of type np.float32 and pass it into cv.warpAffine() function. 
# Below we are doing a shift of (100,50)
#

img = cv.imread( "cars.jpg", 0 )
rows,cols = img.shape

M = np.float32( [[1, 0, 100], [0, 1, 50]] )
dst = cv.warpAffine( img, M, ( cols, rows ) )

cv.imshow( "Translation", dst )
cv.waitKey(0)
cv.destroyAllWindows()


