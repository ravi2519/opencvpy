import numpy as py
import cv2 as cv

img = cv.imread( "cars.jpg" )

#########
# pixel values by row and column cordinates.
# this will return values in BGR e.g. [ 87, 88, 166 ]
px = img[100, 100]
print ( px )

#########

#########
# accessing only blue pixels
blue = img[100, 100, 0]
print ( blue )

#########
# pixel values at certain location can also be modified in similar way
img[ 100, 100 ] = [ 255, 255, 255 ]
print ( img[ 100, 100 ] )

#########
# using numpy is a better way to do all the above
# access RED value using numpy array.item()
red = img.item( 10, 10, 2 )
print ( red )

#########
#modify the RED using numpy array.itemset()
img.itemset( ( 10, 10, 2 ), 100 )
print ( img.item( 10, 10, 2 ) )


