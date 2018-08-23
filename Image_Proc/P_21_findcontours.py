import numpy as np
import cv2 as cv

img = cv.imread( "../resources/drawing.jpg" )

##########
# Contours
# --------
# Contours can be explained simply as a curve joining all the continuous points (along the 
# boundary), having same color or intensity. The contours are a useful tool for shape 
# analysis and object detection and recognition.
#
# - For accuracy use binary images. So apply threshold and canny edge detection before finding contours
# - Since opencv 3.2, findContours() doesn't modify the orginal image.
# - In OpenCV, finding contours is like finding white object from the black background,
#   So object to be found should be white and background should be black.
#
# findContours() has three arguments:
# - source image
# - contour retrieval mode
# - contour approximation method
# 
# It returns three values:
# - modified image
# - the contours - each contour is a numpy array of (x, y) coordinates of boundary 
# - hierarchy
#
# Folloing code find contours

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
ret, thresh = cv.threshold(imgray, 127, 255, 0 )
#thresh = cv.Canny( thresh, 100, 200 )

cv.imshow( "All Contours", thresh )
cv.waitKey(0)
cv.destroyAllWindows()
im2, contours, hierarchy = cv.findContours( thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE )

print( contours )
print( hierarchy )


#
# Drawing Contours
# To draw the contours, cv.drawContours function is used. It can also be used to draw any shape
# provided you have its boundary points. Its first argument is source image, second argument is the contours 
# which should be passed as a Python list, third argument is index of contours (useful when drawing individual 
# contour. To draw all contours, pass -1) and remaining arguments are color, thickness etc.
#

# To draw all the contours in an image:
cv.drawContours(img, contours, -1, (0,255,0), 3)

cv.imshow( "All Contours", img )
cv.waitKey(0)
cv.destroyAllWindows()

# To draw an individual contour, say 4th contour:
cv.drawContours(img, contours, 3, (0,255,0), 3)

cv.imshow( "4th Contour", img )
cv.waitKey(0)
cv.destroyAllWindows()

# But most of the time, below method will be useful:
cnt = contours[4]
print( cnt )
cv.drawContours(img, [cnt], 0, (0,255,0), 3)

cv.imshow( "4th Contour", img )
cv.waitKey(0)
cv.destroyAllWindows()

