import numpy as np
import cv2
import matplotlib.pyplot as plt

# Image Addition
'''
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))		# 250 + 10 = 260 => 255
print(x + y)				# 250 + 10 = 260 % 256 => 4
'''

# Image Blending
'''
img1 = cv2.imread('image.png')
img2 = cv2.imread('opencvLogo.png')
img1 = cv2.resize(img1, (500, 500), interpolation = cv2.INTER_CUBIC)
img2 = cv2.resize(img2, (500, 500), interpolation = cv2.INTER_CUBIC)
dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
cv2.imshow('window', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# Bitwise Operators
img1 = cv2.imread('image.png')
img2 = cv2.imread('opencvLogo.png')
img2 = cv2.resize(img2, (100, 100), interpolation = cv2.INTER_CUBIC)
rows, cols = img2.shape[:2]
roi = img1[0:rows, 0:cols]

imgray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(imgray, 155, 255, cv2.THRESH_BINARY_INV)
ret, mask_inv = cv2.threshold(imgray, 155, 255, cv2.THRESH_BINARY)

img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
'''
cv2.imshow('window', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
plt.subplot(231), plt.imshow(mask), plt.xticks([]), plt.yticks([])
plt.subplot(232), plt.imshow(mask_inv), plt.xticks([]), plt.yticks([])
plt.subplot(233), plt.imshow(img1_bg), plt.xticks([]), plt.yticks([])
plt.subplot(234), plt.imshow(img2_fg), plt.xticks([]), plt.yticks([])
plt.subplot(235), plt.imshow(dst), plt.xticks([]), plt.yticks([])
plt.subplot(236), plt.imshow(img1), plt.xticks([]), plt.yticks([])

plt.show()
