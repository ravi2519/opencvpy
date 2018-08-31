import numpy as np
import cv2 as cv

##########
# A circle is represented mathematically as (x−xcenter)^2+(y−ycenter)^2=r2
# where ( xcenter, ycenter ) is the center of the circle, and r is the radius of the circle.
# Since we have three parameters from the equation, we have to use 3D accumulator for hough transform.
# Which would be highly ineffective. So openCV uses a more trickier method, Hough Gradient Method.
# It uses the gradient information of edges.
#
# cv.HoughCircles()
# Arguments:
#   img - grayscale input image
#   method - Detection method, presently only cv.HOUGH_GRADIENT is supported
#   dp - Inverse ratio of the accumulator resolution to the image resolution. For example, if dp=1 , 
#         the accumulator has the same resolution as the input image. If dp=2 , the accumulator has half as big width and height.
#   minDist - Minimum distance between the centers of the detected circles.If the parameter is too small, multiple neighbor
#             circles may be falsely detected in addition to a true one. If it is too large, some circles may be missed.
#   param1 - higher threshold of the two passed to the Canny edge detector
#   param2 - it is the accumulator threshold for the circle centers at the detection stage. Smaller causes more false circles
#   minRadius - Min circle radius
#   maxRadius - Max circle radius
#

img = cv.imread( "../resources/opencv_logo.png" )
img = cv.cvtColor( img, cv.COLOR_BGR2GRAY )
img = cv.medianBlur( img, 5 )
cimg = cv.cvtColor( img, cv.COLOR_GRAY2BGR )
cv.imwrite("cimg.jpg",cimg)
circles = cv.HoughCircles( img, cv.HOUGH_GRADIENT, 1, 10, param1 = 40, param2 = 10, minRadius = 0, maxRadius = 0 )

circles = np.uint16( np.around(circles) )

for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()
