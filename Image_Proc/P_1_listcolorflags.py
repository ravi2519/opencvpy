import cv2 as cv

##########
# There are more that 150 colorspace conversion flags in OpenCV.
# Here is a list of all of them
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print( flags )
