import numpy as py
import cv2 as cv

img = cv.imread( "cars_1.jpg" )


##########
# Sometimes, you will have to play with certain region of images.
# For eye detection in images, first face detection is done all over the image. 
# When a face is obtained, we select the face region alone and search for 
# eyes inside it instead of searching the whole image. It improves accuracy 
# (because eyes are always on faces :D ) and performance (because we search in a small area).

# ROI is again obtained using numpy indexing
# In below lines of code, we are copying the wheel in the bonnet of the car

wheel = img[ 105:155, 140:180 ]
img[ 50:100, 50:90 ] = wheel

cv.imshow( "Wheel", img )
cv.waitKey(0)
cv.destroyAllWindows()
