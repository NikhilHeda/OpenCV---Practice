import numpy as np
import cv2

# Playing Video from Camera

# cv2.VideoCapture()
# cv2.cvtColor()

# VideoCapture Object methods : 
# isOpened()
# open()
# read()
# release()
'''
cap = cv2.VideoCapture(0) # 0, -1 : for one camera

while True:
	if not cap.isOpened():
		cap.open()
	
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
	cv2.imshow('frame', gray)
	
	# if cv2.waitKey(1) & 0xFF == ord('q'):
	#	break
	# or
	
	k = cv2.waitKey(1) # 1 millisecod wait to display image, not 0 because 0 is indefinite wait.
	if  k == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
'''

# VideoCapture Object methods : 
# get()
# set()
'''
cap = cv2.VideoCapture(0)

while cap.isOpened:
	
	ret, frame = cap.read()
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
	
	ret = cap.set(3, 320)	# frame width
	ret = cap.set(4, 240) # frame height
	
	cv2.imshow('frame', gray)
	
	k = cv2.waitKey(1)
	if  k == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
'''

# Playing Video from file
'''
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened:
	
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
	cv2.imshow('frame', gray)
	
	k = cv2.waitKey(25)
	if  k == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
'''

# Saving a Video

# cv2.VideoWriter()
# cv2.VideoWriter_fourcc()
# cv2.flip()

# VideoWriter Object methods : 
# write()

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('saved_video.mp4', fourcc, 20.0, (640, 480) )

while cap.isOpened():
	ret, frame = cap.read();
	if ret:
		frame = cv2.flip(frame, 1) # 1 : flip horizontally; 0 : flip vertically
		cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame',frame)
		out.write(frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows()
