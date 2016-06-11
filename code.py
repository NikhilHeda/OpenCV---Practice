import cv2
import numpy as np

img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,50,150,apertureSize = 3)

'''
lines = cv2.HoughLines(edges,1,np.pi/180,140)
for line in lines:
	for rho,theta in line:
		a = np.cos(theta)
		b = np.sin(theta)
		x0 = a*rho
		y0 = b*rho
		x1 = int(x0 + 1000*(-b))
		y1 = int(y0 + 1000*(a))
		x2 = int(x0 - 1000*(-b))
		y2 = int(y0 - 1000*(a))

		cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
'''

minLineLength = 150
maxLineGap = 10

lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for line in lines:
	for x1,y1,x2,y2 in line:
		cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
