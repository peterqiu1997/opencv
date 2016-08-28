import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


img = cv.imread("./cvpics/messi.jpg", 0)
plt.imshow(img, cmap = "gray", interpolation = "bicubic")
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
cv.imshow('messi', img)
cv.waitKey(0)
cv.destroyAllWindows()