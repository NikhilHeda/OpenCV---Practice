import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('j.png')

# Erosion
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)

# Dilation
dilation = cv2.dilate(img,kernel,iterations = 1)

# Opening
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Top Hat
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Black Hat
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

titles = ['Original Image','Erosion','Dilation','Opening','Closing','Gradient', 'Top Hat', 'Black Hat']
images = [img, erosion, dilation, opening, closing, gradient, tophat, blackhat]

for i in range(8):
    plt.subplot(2, 4, i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

# Structuring Element

# Rectangular Kernel
print(cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)))

# Elliptical Kernel
print(cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))

# Cross-shaped Kernel
print(cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)))
