import numpy as np
import cv2

img = cv2.imread('cvpics/sudoku.png', 0)

img = cv2.medianBlur(img, 5)
gaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('img', img)
cv2.imshow('Gaussian', gaussian)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()


