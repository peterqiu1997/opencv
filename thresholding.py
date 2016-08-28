import numpy as np 
import cv2 
#from matplotlib import pyplot as plt 

#matplotlib.use('tkagg')

img = cv2.imread('cvpics/gradient.jpg', 0)
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('BINARY', thresh1)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
