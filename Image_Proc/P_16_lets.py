import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread( "../resources/noisy.png" )

blur = cv.GaussianBlur( img, (5,5), 0 )
kernel = np.ones( (3,3), np.uint8 )

dst = cv.erode( blur, kernel, iterations = 1 )

#dst = cv.cvtColor( dst, cv.COLOR_BGR2GRAY )

#th2 = cv.adaptiveThreshold( dst, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2 )

plt.subplot( 121 ), plt.imshow(img), plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot( 122 ), plt.imshow(dst), plt.title('Erode')
plt.xticks([]),plt.yticks([])
plt.show()

