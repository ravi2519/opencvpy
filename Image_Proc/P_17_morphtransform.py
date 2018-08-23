import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread( "../resources/j.png", 0 )

##########
# Morphological Transformations
# -----------------------------
#
# Morphological transformations are some simple operations based on the image shape. 
# It is normally performed on binary images. It needs two inputs, one is our original image, 
# second one is called structuring element or kernel which decides the nature of operation. 
# Two basic morphological operators are Erosion and Dilation. Then its variant forms like Opening, 
# Closing, Gradient etc also comes into play.  
#
# 1. Erosion
# ----------
# It erodes away the foreground object. ( VV Imp : Always keep the foreground object in white )
# The kernel slides through the image (as in 2D convolution). A pixel in the original image (either 1 or 0)
# will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
# So what happends is that, all the pixels near boundary will be discarded depending upon the size of kernel.
# So the thickness or size of the foreground object decreases or simply white region decreases in the image. 
# It is useful for removing small white noises (as we have seen in colorspace chapter), detach two connected objects etc.
#

kernel = np.ones( ( 5, 5 ), np.uint8 )
erosion = cv.erode( img, kernel, iterations = 1 )



#
# 2. Dilation
# -----------
# It is just opposite of erosion. Here, a pixel element is '1' if atleast one pixel under the kernel is '1'. 
# So it increases the white region in the image or size of foreground object increases. Normally, in cases like noise removal, 
# erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. 
# Since noise is gone, they won't come back, but our object area increases. It is also useful in joining broken parts of an object.
#

dilation = cv.dilate( img, kernel, iterations = 1 )


#
# 3. Opening
# ----------
# Opening is just another name of erosion followed by dilation. It is useful in removing noise, 
# as we explained above. Here we use the function, cv.morphologyEx()
# 

img2 = cv.imread( "../resources/j2.png", 0)
opening = cv.morphologyEx( img2, cv.MORPH_OPEN, kernel )

#
# 4. Closing
# ----------
# Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small 
# holes inside the foreground objects, or small black points on the object.
#

img3 = cv.imread( "../resources/j3.png", 0 )
closing = cv.morphologyEx( img3, cv.MORPH_CLOSE, kernel )

#
# 5. Morphological Gradient
# -------------------------
# It is the difference between dilation and erosion.
#

gradient = cv.morphologyEx ( img, cv.MORPH_GRADIENT, kernel )

#
# 6. Top Hat
# ----------
# It is the difference between input image and the Opening of the image
#

kernel2  = np.ones( (9, 9), np.uint8 )
tophat = cv.morphologyEx ( img, cv.MORPH_TOPHAT, kernel2 )

#
# 7. Black Hat
# ------------
# It i sthe difference between input image and the Closing of an image

blackhat = cv.morphologyEx( img, cv.MORPH_BLACKHAT, kernel )

# Plotting the results

plt.subplot( 721 ), plt.imshow( img ), plt.title( "Original" )
plt.xticks([]), plt.yticks([])
plt.subplot( 722 ), plt.imshow( erosion ), plt.title( "Erosion" )
plt.xticks([]), plt.yticks([])
plt.subplot( 723 ), plt.imshow( img ), plt.title( "Original" )
plt.xticks([]), plt.yticks([])
plt.subplot( 724 ), plt.imshow( dilation ), plt.title( "Dilation" )
plt.xticks([]), plt.yticks([])
plt.subplot( 725 ), plt.imshow( img2 ), plt.title( "Original" )
plt.xticks([]), plt.yticks([])
plt.subplot( 726 ), plt.imshow( opening ), plt.title( "Opening" )
plt.xticks([]), plt.yticks([])
plt.subplot( 727 ), plt.imshow( img3 ), plt.title( "Original" )
plt.xticks([]), plt.yticks([])
plt.subplot( 728 ), plt.imshow( closing ), plt.title( "Closing" )
plt.xticks([]), plt.yticks([])
plt.subplot( 729 ), plt.imshow( img ), plt.title( "Original" )
plt.xticks([]), plt.yticks([])
plt.subplot( 7,2,10 ), plt.imshow( gradient ), plt.title( "Gradient" )
plt.xticks([]), plt.yticks([])
plt.subplot( 7,2,11 ), plt.imshow( img ), plt.title( "Original" )
plt.xticks([]), plt.yticks([])
plt.subplot( 7,2,12 ), plt.imshow( tophat ), plt.title( "Tophat" )
plt.xticks([]), plt.yticks([])
plt.subplot( 7,2,13 ), plt.imshow( img ), plt.title( "Original" )
plt.xticks([]), plt.yticks([])
plt.subplot( 7,2,14 ), plt.imshow( blackhat ), plt.title( "Blackhat" )
plt.xticks([]), plt.yticks([])

plt.show()
