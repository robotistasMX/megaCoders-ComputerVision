import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    filtro1 = cv2.erode(mask, cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)), iterations=1)
    filtro2 = cv2.erode(filtro1, cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)), iterations=1)
    
    objct = cv2.moments(filtro2)
    if objct['m00'] > 50000:
        cx = int(objct['m10']/objct['m00'])
        cy = int(objct['m01']/objct['m00'])
        cv2.circle(frame, (cx,cy), 10, (0,0,255), 4)


    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()