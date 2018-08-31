import numpy as np
import cv2 as cv


##########
# Now we know how to convert BGR image to HSV( Hint: cvtColor ), we can use this to extract a colored object. 
# In HSV, it is more easier to represent a color than in BGR color-space. 
# In our application, we will try to extract a blue colored object.
# Following steps will be taken to do that:
#   -> Take each frame of the video
#   -> Convert from BGR to HSV color-space
#   -> We threshold the HSV image for a range of blue color
#   -> Now extract the blue object alone, we can do whatever on that image we want.


# capture a video file, a running video file can also be loaded
# we just need to leave the arguments to blank
cap = cv.VideoCapture( "blue_object.mp4" )

while(1):

    # take each frame
    _, frame = cap.read()

    # convert BGR to HSV
    hsv = cv.cvtColor( frame, cv.COLOR_BGR2HSV )

    # define range of blue color in HSV
    # how we reached these values is demonstrated in P_4 
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # threshold the HSV image to get only blue colors
    mask = cv.inRange( hsv, lower_blue, upper_blue )

    # bitwise AND mask and original image
    res = cv.bitwise_and( frame, frame, mask = mask )

    cv.imshow( 'frame', frame )
    cv.imshow( 'mask', mask )
    cv.imshow( 'res', res )

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()

