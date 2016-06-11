import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)

# colors
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
yellow = (0, 255, 255)
unknown = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
gray = 10

'''
# line
cv2.line(img, (0, 0), (511, 511), blue, 5)
cv2.line(img, (511, 0), (0, 511), blue, 5)

# rectangle
cv2.rectangle(img, (127, 127), (383, 383), green, 3)

# circle
cv2.circle(img, (254, 254), 128, red, 3, cv2.LINE_AA)

# ellipse
cv2.ellipse(img, (254, 304), (256, 128), 0, 0, 180, yellow, 3, cv2.LINE_AA)
cv2.ellipse(img, (254, 204), (256, 128), 180, 0, 180, yellow, 3, cv2.LINE_AA)

# polygon
pts = np.array([ [254, 0], [447, 254], [254, 511], [63, 254]], np.int32)
pts = np.reshape(pts, (-1, 1, 2))
cv2.polylines(img, [pts], True, unknown)

# text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Open CV', (50, 500), font, 3, white, 2, cv2.LINE_AA)
'''

# Open CV logo
img = np.zeros((612, 512, 3), np.uint8) 
img[:] = white	# setting each pixel to white

circle_radius = 118

start_angle = 180
cv2.ellipse(img, (255, 127), (circle_radius, circle_radius), start_angle, -60, 240, red, -1, cv2.LINE_AA)
cv2.ellipse(img, (255, 127), (circle_radius - 70, circle_radius - 70), start_angle, -62, 242, white, -1, cv2.LINE_AA)

start_angle = 60
cv2.ellipse(img, (127, 348), (circle_radius, circle_radius), start_angle, -60, 240, green, -1, cv2.LINE_AA)
cv2.ellipse(img, (127, 348), (circle_radius - 70, circle_radius - 70), start_angle, -62, 242, white, -1, cv2.LINE_AA)

start_angle = 0
cv2.ellipse(img, (383, 348), (circle_radius, circle_radius), start_angle, -60, 240, blue, -1, cv2.LINE_AA)
cv2.ellipse(img, (383, 348), (circle_radius - 70, circle_radius - 70), start_angle, -62, 242, white, -1, cv2.LINE_AA)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (75, 550), font, 3, black, 4, cv2.LINE_AA)

cv2.imshow('My Drawing', img)
cv2.imwrite('opencvLogo.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
