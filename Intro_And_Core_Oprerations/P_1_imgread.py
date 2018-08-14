import numpy as np
import cv2 as cv

# reads an image in grayscale
# other methods are:
#   cv.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
#   cv.IMREAD_GRAYSCALE : Loads image in grayscale mode
#   cv.IMREAD_UNCHANGED : Loads image as such including alpha channel
img = cv.imread('cars.jpg',0)

# show an image in the window named "image"
cv.imshow('image', img)

# keyboard binding function. Its argument is the time in milliseconds. The function waits for specified milliseconds for any keyboard event. If you press any key in that time, the program continues. If 0 is passed, it waits indefinitely for a key stroke. It can also be set to detect specific key strokes like, if key a is pressed etc which we will discuss below.
cv.waitKey(0)

#simply destroys all the windows we created. If you want to destroy any specific window, use the function cv.destroyWindow() where you pass the exact window name as the argument.
cv.destroyAllWindows()
