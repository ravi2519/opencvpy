import numpy as np
import cv2 as cv

img = cv.imread( "cars.jpg", 0 )
cv.imshow("image", img)

# NOTE: remember to use following when on 64-bit machine
# k = cv.waitKey(0) & 0xFF
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('cars_gray.jpg', img)
    cv.destroyAllWindows()
