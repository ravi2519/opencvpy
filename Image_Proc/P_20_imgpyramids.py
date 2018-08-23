import cv2 as cv
import numpy as np,sys

##########
# Image Pyramids
# --------------
# Normally, we used to work with an image of constant size. But on some occasions, 
# we need to work with (the same) images in different resolution. For example, while searching for 
# something in an image, like face, we are not sure at what size the object will be present in said image.
# In that case, we will need to create a set of the same image with different resolutions 
# and search for object in all of them.These set of images with different resolutions are called Image 
# Pyramids (because when they are kept in a stack with the highest resolution image at the 
# bottom and the lowest resolution image at top, it looks like a pyramid).
#
# There are two kinds of Image Pyramids. 1) Gaussian Pyramid and 2) Laplacian Pyramids
# 
# Higher level (Low resolution) in a Gaussian Pyramid is formed by removing consecutive rows 
# and columns in Lower level (higher resolution) image. Then each pixel in higher level is formed by the 
# contribution from 5 pixels in underlying level with gaussian weights. By doing so, a M×N image becomes 
# M/2×N/2  image. So area reduces to one-fourth of original area. It is called an Octave. The same pattern 
# continues as we go upper in pyramid (ie, resolution decreases). Similarly while expanding, area becomes 4
# times in each level. We can find Gaussian pyramids using cv.pyrDown() and cv.pyrUp() functions.
#
#
# Laplacian Pyramids are formed from the Gaussian Pyramids. There is no exclusive function for that. 
# Laplacian pyramid images are like edge images only. Most of its elements are zeros. They are used in image compression.
# A level in Laplacian Pyramid is formed by the difference between that level in Gaussian Pyramid and expanded
# version of its upper level in Gaussian Pyramid.
#
# One application of this is Image Blending. For example, in image stitching, you will need to stack 
# two images together, but it may not look good due to discontinuities between images. In that case,
# image blending with Pyramids gives you seamless blending without leaving much data in the images. One 
# Here are the steps to do that:
# 1. Load two images.
# 2. Find the Gaussian Pyramids of both images.
# 3. From Guassin Pyramids, find their Laplacian Pyramids.
# 4. Now join the left half of image 1 with the right half of image 2 in each level of Laplacian Pyramids.
# 5. Finally from this joint image pyramids, reconstruct the original image.
#
#

A = cv.imread( "../resources/image1.jpg" )
B = cv.imread( "../resources/image2.jpg" )

# Generate the Guassian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(gpA[i])
    gpA.append(G)

# Generate the Guassian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(gpB[i])
    gpB.append(G)

# Generate the Laplacian Pyramid for A
lpA = [ gpA[5] ]
for i in range( 5, 0, -1 ):
    size = (gpA[i-1].shape[1], gpA[i-1].shape[0])
    GE = cv.pyrUp( gpA[i], dstsize = size )
    L = cv.subtract( gpA[i-1], GE )
    lpA.append( L )

# Generate the Laplacian Pyramid for B
lpB = [ gpB[5] ]
for i in range( 5, 0, -1 ):
    size = (gpB[i-1].shape[1], gpB[i-1].shape[0])
    GE = cv.pyrUp( gpB[i], dstsize = size )
    L = cv.subtract( gpB[i-1], GE )
    lpB.append( L )

# Now add left and right halves of images in each level
LS = []
for la, lb in zip( lpA, lpB ):
    rows, cols, dpt = la.shape
    nr_cols_1 = cols/2
    nr_cols_2 = cols/2
    ls = np.hstack( ( la[:,0:nr_cols_1], lb[:,nr_cols_2:] ) )
    LS.append( ls )

# Now reconstruct
ls_ = LS[0]
for i in range( 1, 6 ):
    size = (LS[i].shape[1], LS[i].shape[0])
    ls_ = cv.pyrUp( ls_, dstsize = size )
    ls_ = cv.add( ls_, LS[i] )

# image with direct connecting each half
real = np.hstack( ( A[:,:cols/2], B[:,cols/2:] ) )

cv.imwrite( "Pyramid_blending2.jpg", ls_ )
cv.imwrite( "Direct_blending.jpg", real )
