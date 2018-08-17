import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img=cv.imread("../resources/sudoku.jpg")
plt.subplot(121), plt.imshow(img), plt.title("Input")
plt.show()
