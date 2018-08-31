import numpy as np
import cv2 as cv

##########
# Hough Transform
# ---------------
# Head to medium to understand this better:
# https://medium.com/@tempflip/lane-detection-with-numpy-2-hough-transform-f4c017f4da39
# 
# OpenCV has two methods to get Hough Lines:
# 1. cv.HoughLines
#   It simply returns an array of :math:(rho, theta)` values. ρ is measured in pixels and θ is measured in radians.
#   First parameter, Input image should be a binary image, so apply threshold or use canny edge detection before applying 
#   hough transform. Second and third parameters are ρ and θ accuracies respectively. 
#   Fourth argument is the threshold, which means the minimum vote it should get to be considered as a line.
#   Number of votes depends upon the number of points on the line. So it represents the minimum length of line that should be detected.
#
# 

img = cv.imread( "../resources/sudoku.png" )
gray = cv.cvtColor( img, cv.COLOR_BGR2GRAY )
edges = cv.Canny( gray, 50, 150, apertureSize = 3 )


lines = cv.HoughLines( edges, 1, np.pi/180, 200 )
for line in lines:
    rho, theta = line[0]
    a = np.cos( theta )
    b = np.sin( theta )
    x0 = a*rho
    y0 = b*rho
    x1 = int( x0 + 1000*(-b) )
    y1 = int( y0 + 1000*(a) )
    x2 = int( x0 - 1000*(-b) )
    y2 = int( y0 - 1000*(a) )

    cv.line( img, (x1, y1 ), (x2, y2), (0,0,255), 1 )

cv.imwrite( 'houhlines.jpg', img )


#
# 2. Probablistic Hough Transform ( cv.HoughLinesP )
#   In the hough transform, you can see that even for a line with two arguments, it takes a lot of computation.
#   Probabilistic Hough Transform is an optimization of the Hough Transform we saw. It doesn't take all the points into consideration.
#   Instead, it takes only a random subset of points which is sufficient for line detection. Just we have to decrease the threshold.
#   
#   http://phdfb1.free.fr/robot/mscthesis/node14.html
#
#   Two arguments:
#       minLineLength: Minimum length of line. Line segments shorter than this are rejected.
#       maxLineGap : Maximum allowed gap between line segments to treat them as a single line.
#
#   Best thing is this directly returns two endpoints of line.
#
img2 = cv.imread( "../resources/sudoku.png" )
gray2 = cv.cvtColor( img2, cv.COLOR_BGR2GRAY )
edges2 = cv.Canny( gray, 50, 150, apertureSize = 3 )
lines = cv.HoughLinesP( edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10 )
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line( img, (x1,y1), (x2, y2), (0, 255, 0), 2)

cv.imwrite( "houghlines2.jpg", img)


