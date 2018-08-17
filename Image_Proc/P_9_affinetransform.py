import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread( "drawing.jpg" )
rows, cols, c = img.shape

##########
# In affine transformation, all parallel lines in the original image will still be 
# parallel in the output image. To find the transformation matrix, we need three 
# points from input image and their corresponding locations in output image. 
# Then cv.getAffineTransform will create a 2x3 matrix which is to be passed to cv.warpAffine.
#

pts1 = np.float32([[180, 85], [88,266], [264,197]])
pts2 = np.float32([[10, 115], [200,466], [400,100]])

M = cv.getAffineTransform( pts1, pts2 )

dst = cv.warpAffine( img, M, ( cols, rows ) )

plt.subplot(121), plt.imshow(img), plt.title("Input")
plt.subplot(122), plt.imshow(dst), plt.title("Output")
plt.show()

