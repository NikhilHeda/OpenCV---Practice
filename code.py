import numpy as np
import cv2
import matplotlib.pyplot as plt
'''
img = cv2.imread('../Assets/image.png')

# accessing image pixels
px = img[200, 200]
print(px)

# accessing only blue values
blue = img[200, 200, 0]
print(blue)

# modifying one pixel value
img[200, 200] = 0

# modifying a region of pixels
img[200:200, 200:200] = 0

# Numpy Indexing : faster
# Accessing
print(img.item(20, 20, 2))

# Modifying
img.itemset((20, 20, 2), 200)
print(img.item(20, 20, 2))

# Accessing Image properties:
print("Image Shape :", img.shape)
print("Image Size :", img.size)
print("Image Data Type :", img.dtype)

# Region of image
region = img[200:201, 300:401] = 0
img = region

imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB)
plt.xticks([])
plt.yticks([])
plt.show()

cv2.destroyAllWindows()
'''

RED = [255,0,0]

img1 = cv2.imread('../Assets/image.png')

replicate = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_CONSTANT,value = RED)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()