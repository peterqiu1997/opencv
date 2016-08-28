import numpy as np
import cv2
import math

"""
 USING: HSV MODEL
 CALC-HISTOGRAM: DRAW HAND SHAPE
 BACK PROJECT
 MASK
 LARGEST CONTOUR 
 READ CONVEXITY DEFECTS 
"""
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    cv2.rectangle(img,(300,300),(100,100),(0,255,0),0)
    cropped = img[100:300, 100:300]
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7), 0)
    ret, thresh1 = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # returns additional image for chaining purposes, but is useless since it modifies original image
    cont_img, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    for i in range(len(contours)):
            cnt = contours[i]
            area = cv2.contourArea(cnt)
            if(area > max_area):
                max_area = area
                ci = i
    cnt = contours[ci]
    #x,y,w,h = cv2.boundingRect(cnt)
    #cv2.rectangle(cropped,(x,y),(x+w,y+h),(0,0,255),0)
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(cropped.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
    cv2.drawContours(drawing,[hull],0,(0,0,255),2)
    hull = cv2.convexHull(cnt, returnPoints = False)
    defects = cv2.convexityDefects(cnt, hull)
    count_defects = 0
    """for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        if angle <= 90:
            count_defects += 1
            cv2.circle(cropped,far,1,[0,0,255],-1)
        #dist = cv2.pointPolygonTest(cnt,far,True)
        cv2.line(cropped,start,end,[0,255,0],2)
        #cv2.circle(crop_img,far,5,[0,0,255],-1)"""
    cv2.drawContours(img, contours, -1, (255,0,255), 3, offset = (100, 100))
    cv2.imshow('Final', img)
    k = cv2.waitKey(10)
    if k == 27:
        break

