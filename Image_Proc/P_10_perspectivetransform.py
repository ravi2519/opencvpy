import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread( "doc.jpg" )
rows,cols,ch = img.shape
print( "Rows=" + str(rows) + "; cols=" + str(cols) )

##########
# Perspective Transaformation is how we straighten up documents in image processing applications.
# Both Affine Tranformation and Prespective Transformation is used for this purpose.
#
# For perspective transformation, you need a 3x3 transformation matrix. 
# Straight lines will remain straight even after the transformation. 
# To find this transformation matrix, you need 4 points on the input image and corresponding points 
# on the output image. Among these 4 points, 3 of them should not be collinear. 
# Then transformation matrix can be found by the function cv.getPerspectiveTransform. 
# Then apply cv.warpPerspective with this 3x3 transformation matrix.


pts1 = np.float32([[637,88],[1500,158],[540,2480],[1400,2545]]) # points on the source image that form document boundary
pts2 = np.float32([[0,0],[800,0],[0,2400],[800,2400]]) # points on the dest image

M = cv.getPerspectiveTransform(pts1, pts2) # M is the transform matrix

# args are source image, tranform matrix and dest image size
dst = cv.warpPerspective( img, M, ( 800, 2400 ) )

plt.subplot(121),plt.imshow(img),plt.title("Input")
plt.subplot(122),plt.imshow(dst),plt.title("Output")

plt.show()
