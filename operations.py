import cv2 
import numpy as np

img = cv2.imread('cvpics/messi.jpg')

print(img.shape)

px = img[400, 600]
print(px[0])
print(img.item(400, 600, 0))