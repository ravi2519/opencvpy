import numpy as np
import cv2 as cv

blue = np.uint8( [[[255, 0, 0]]] )
hsv_blue = cv.cvtColor( blue, cv.COLOR_BGR2HSV )
print( hsv_blue ) # [ 120, 255, 255 ]

# Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively.
