import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(True):
    _ , frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    mask = cv.inRange(hsv, lower_blue,upper_blue )
    
    filtro1 = cv.erode(mask, cv.getStructuringElement(cv.MORPH_RECT,(3,3)), iterations=1)
    filtro2 = cv.erode(filtro1, cv.getStructuringElement(cv.MORPH_RECT,(5,5)), iterations=1)
    
    objct = cv.moments(filtro2)
    if objct['m00'] > 50000:
        cx = int(objct['m10']/objct['m00'])
        cy = int(objct['m01']/objct['m00'])
        cv.circle(frame, (cx,cy), 10, (0,0,255), 4)
        
    cv.imshow('original', frame)
    cv.imshow('azul', filtro2)
    k = cv.waitKey(5) 
    if k == 27:
        break
cv.destroyAllWindows()