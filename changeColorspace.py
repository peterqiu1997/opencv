import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read() # boolean, frame returned from read

    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # change color spaces

        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        output = cv2.bitwise_and(frame, frame, mask = mask)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('output',output)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()