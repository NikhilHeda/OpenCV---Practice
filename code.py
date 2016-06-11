import numpy as np
import cv2

def callback(x):
	pass

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('R', 'image', 0, 255, callback)
cv2.createTrackbar('G', 'image', 0, 255, callback)
cv2.createTrackbar('B', 'image', 0, 255, callback)
switch = "0: OFF\n1: ON"
cv2.createTrackbar(switch, 'image', 0, 1, callback)

while True:
	cv2.imshow('image', img)
	
	r = cv2.getTrackbarPos('R', 'image')
	g = cv2.getTrackbarPos('G', 'image')
	b = cv2.getTrackbarPos('B', 'image')
	s = cv2.getTrackbarPos(switch, 'image')
	
	if s == 0:
		img[:] = 0
	else:
		img[:] = (b, g, r)
		
	if cv2.waitKey(20) == ord('q'):
		break
		
cv2.destroyAllWindows()