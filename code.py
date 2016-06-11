import numpy as np
import cv2

# cv2.imread()
'''
imgRGB = cv2.imread('image.png', -1) # Default
imgGRAY = cv2.imread('image.png', 0)
imgALPHA = cv2.imread('image.png', 1)
'''

# cv2.imshow()
# cv2.waitKey()
# cv2.destroyAllWindows()
# cv2.destroyWindow()
'''
imgRGB = cv2.imread('image.png', -1) # Default
imgGRAY = cv2.imread('image.png', 0)
imgALPHA = cv2.imread('image.png', 1)
cv2.imshow('Color Image', imgRGB)
cv2.imshow('Grayscale Image', imgGRAY)
cv2.imshow('Alpha Image', imgALPHA)

cv2.waitKey(1000) # Indefinitely wait for a keyboard event
# cv2.destroyAllWindows()
cv2.destroyWindow('Alpha Image') 
'''

#cv2.namedWindow()
'''
imgRGB = cv2.imread('image.png')
cv2.namedWindow('Color Image', cv2.WINDOW_NORMAL) # Resizeable
# cv2.namedWindow('Color Image', cv2.WINDOW_AUTOSIZE) # Not Resizeable - Default
cv2.imshow('Color Image', imgRGB)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# cv2.imwrite()
'''
imgGRAY = cv2.imread('image.png', 0)
cv2.imwrite('saved_image.png', imgGRAY);
'''

# Summary
'''
imgGRAY = cv2.imread('image.png', 0)
cv2.imshow('Display Image', imgGRAY)
k = cv2.waitKey(0)
if k == 27:		# if 'esc' is pressed quit without saving
	cv2.destroyAllWindows()
elif k == ord('s'): # else if 's' is pressed : save the image.
	cv2.imwrite('saved_image.png', imgGRAY)
	cv2.destroyAllWindows()
'''

# using matplotlib

# Displaying grayscale image
'''
import matplotlib.pyplot as plt

img = cv2.imread('image.png', 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([])
plt.yticks([])
plt.show()
'''

# Displaying color image - 1st approach
'''
import matplotlib.pyplot as plt

def display_image(image):
	plt.imshow(image, interpolation = 'bicubic')
	plt.xticks([])
	plt.yticks([])
	plt.show()
	
imgBGR = cv2.imread('image.png')
(B, G, R) = cv2.split(imgBGR)
imgRGB = cv2.merge([R, G, B])
display_image(imgBGR)
display_image(imgRGB)
'''

# Displaying color image - 2nd approach
import matplotlib.pyplot as plt

imgBGR = cv2.imread('image.png')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB, interpolation = 'bicubic')
plt.xticks([])
plt.yticks([])
plt.show()
