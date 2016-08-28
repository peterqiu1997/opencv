import numpy as np 
import cv2

img = cv2.imread('cvpics/messi.jpg')
print(img.item(400,890,2))
print(img.item(400,890,1))
print(img.item(400,890,0))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(hsv.item(400,400,0))
print(hsv.item(400,400,1))
print(hsv.item(400,400,2))

cv2.imshow('HSV',hsv)
k = cv2.waitKey(0) & 0xFF
if k == 27:
	cv2.destroyAllWindows()