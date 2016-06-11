import cv2
import numpy as np
import matplotlib.pyplot as plt

# cv2.getPerspectiveTransform()
# cv2.warpAffine()
# cv2.warpPrespective()

img = cv2.imread('opencvLogo.png')
rows, cols = img.shape[:2]

# Scaling
'''
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
# OR
height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
'''

# Translation
'''
M = np.float32([ [1, 0, 100], [0, 1, 50] ])
res = cv2.warpAffine(img, M, (cols, rows))
'''

# Rotation
'''
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
res = cv2.warpAffine(img, M, (cols,rows))
'''

# Affine Transformation
'''
pts1 = np.float32([ [50, 50], [200, 50], [50, 200] ])
pts2 = np.float32([ [10, 100], [200, 50], [100, 250] ])

M = cv2.getAffineTransform(pts1, pts2)
res = cv2.warpAffine(img, M, (cols, rows))
'''

# Perspective Transformation
pts1 = np.float32([ [56, 65], [368, 52], [28, 387], [389, 390] ])
pts2 = np.float32([ [0, 0], [300, 0], [0, 300], [300, 300] ])

M = cv2.getPerspectiveTransform(pts1, pts2)

res = cv2.warpPerspective(img, M, (300, 300))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(res), plt.title('Output')
plt.show()
