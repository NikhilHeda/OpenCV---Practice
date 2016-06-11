import numpy as np
import cv2

# cv2.getTickCount()
# cv2.getTickFrequency()

img1 = cv2.imread('image.png')

e1 = cv2.getTickCount()
for i in range(5, 49, 2):
	img1 = cv2.medianBlur(img1, i)
e2 = cv2.getTickCount()
print( (e2 - e1) / cv2.getTickFrequency() )

# IPython
'''
# check if optimization is enabled
In [5]: cv2.useOptimized()
Out[5]: True

In [6]: %timeit res = cv2.medianBlur(img,49)
10 loops, best of 3: 34.9 ms per loop

# Disable it
In [7]: cv2.setUseOptimized(False)

In [8]: cv2.useOptimized()
Out[8]: False

In [9]: %timeit res = cv2.medianBlur(img,49)
10 loops, best of 3: 64.1 ms per loop
'''