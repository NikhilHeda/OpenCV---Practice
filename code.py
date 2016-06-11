import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('opencvLogo.png')

# 2D Convolution (Image Filtering)
'''
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
'''

# Image Blurring
# 1. Averaging
# cv2.blur()
'''
dst = cv2.blur(img, (9, 9))
'''

# Gaussian Blurring
# cv2.GaussianBlur()
# cv2.getGaussianKernel()
'''
dst = cv2.GaussianBlur(img, (5, 5), 0)
'''

# Median Blurring
# cv2.medianBlur()
'''
dst = cv2.medianBlur(img, 5)
'''

# Bilateral Filtering
# cv2.bilateralFilter()

dst = cv2.bilateralFilter(img, 9, 75, 75)


plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.xticks([]), plt.yticks([])
plt.show()
