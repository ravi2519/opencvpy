import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("../resources/noisy6.jpg", 0)

##########
# Earlier in one of the threshold example i told you that there is second parameter retVal. Its use 
# comes when we go for Otsu’s Binarization. So what is it?
#
# In global thresholding, we used an arbitrary value for threshold value, right? 
# So, how can we know a value we selected is good or not? Answer is, trial and error 
# method. But consider a bimodal image (In simple words, bimodal image is an image 
# whose histogram has two peaks). For that image, we can approximately take a value 
# in the middle of those peaks as threshold value, right ? That is what Otsu binarization 
# does. So in simple words, it automatically calculates a threshold value from 
# image histogram for a bimodal image. (For images which are not bimodal, binarization won’t be accurate.)
#
# For this, our cv.threshold() function is used, but pass an extra flag, cv.THRESH_OTSU. 
# For threshold value, simply pass zero. Then the algorithm finds the optimal threshold 
# value and returns you as the second output, retVal. If Otsu thresholding is not used, 
# retVal is same as the threshold value you used.
#
# Check out below example. Input image is a noisy image. In first case, I applied global 
# thresholding for a value of 127. In second case, I applied Otsu’s thresholding directly. 
# In third case, I filtered image with a 5x5 gaussian kernel to remove the noise, 
# then applied Otsu thresholding. See how noise filtering improves the result.
#
#

# global thresholding
ret1, th1 = cv.threshold( img, 127, 255, cv.THRESH_BINARY )

# Otsu's thresholding
ret2, th2 = cv.threshold( img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU )

# Otsu's thresholding after Gaussian filtering
blur = cv.GaussianBlur( img, (5,5), 0 )
ret3, th3 = cv.threshold( blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU )

# plot all the images and their histograms
images = [ img, 0, th1,
            img, 0, th2,
            blur, 0, th3 ]

titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()


