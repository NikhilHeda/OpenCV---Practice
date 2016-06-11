import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

'''
def draw_circle(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img, (x, y), 100, -1)
		
img = np.zeros((512, 512, 3), np.uint8)
img[:] = (255, 255, 255)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
	cv2.imshow('image', img)
	if cv2.waitKey(20) & 0XFF == 25:
		break
	
cv2.destroyAllWindows()
'''

drawing = False			# True : mouse pressed
mode = True				# True : rectangle, False : circle
ix = -1
iy = -1

def draw(event, x, y, flag, params):
	global ix, iy, mode, drawing
	
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix = x
		iy = y
		
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing:
			if mode:
				cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
			else:
				cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
				
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if mode:
			cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
		else:
			cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
			
img = np.zeros((512, 512, 3), np.uint8)
img[:] = (255, 255, 255)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

while True:
	cv2.imshow('image', img)
	k = cv2.waitKey(1) & 0xFF
	if k == ord('m'):
		mode = not mode
	elif k == ord('q'):
		break

cv2.destroyAllWindows()