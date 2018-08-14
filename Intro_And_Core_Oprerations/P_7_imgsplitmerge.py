import numpy as py
import cv2 as cv

img = cv.imread( "cars_P_7.jpg" )


##########
# Sometimes you will need to work separately on B,G,R channels of image.
# In this case, you need to split the BGR images to single channels.
# In other cases, you may need to join these individual channels to a BGR image. You can do it simply by

b,g,r = cv.split( img )
img = cv.merge( ( b,g,r ) )
cv.imshow( "Cars Split and Merge", img )
cv.waitKey(0)
cv.destroyAllWindows()

# Now, something cool you do is like changing the color of car
# A green JEEP
img = cv.merge( ( b,r,g ) )
cv.imshow( "Green JEEP", img )
cv.waitKey(0)
cv.destroyAllWindows()

# A blue JEEP
img = cv.merge( ( r,b,g ) )
cv.imshow( "Blue JEEP", img )
cv.waitKey(0)
cv.destroyAllWindows()


##########
# Numpy indexing can also be used to split individual channels

b = img[:,:,0]

# similarlly suppose you want to set all the red pixels to zero
img = cv.merge( ( b,g,r ) )
img[:,:,2] = 0
cv.imshow( "Red Pixesl to Zero", img )
cv.waitKey(0)
cv.destroyAllWindows()
