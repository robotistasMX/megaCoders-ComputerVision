import cv2
import numpy as np

lower_blue = np.array([98,99,87])
upper_blue = np.array([115,255,255])

lower_pink = np.array([160,50,50])
upper_pink = np.array([180,255,255])

lower_green = np.array([50,100,100])
upper_green = np.array([70,255,255])

lower_red = np.array([0,100,100])
upper_red = np.array([10,255,255])

lower_white = np.array([0,0,100])
upper_white = np.array([0,0,255])

lower_black = np.array([0,0,0])
upper_black = np.array([255,255,55])

cap= cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray',gray)
    blur= cv2.GaussianBlur(frame,(7,7),0)
    #cv2.imshow('blur',blur)
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #cv2.imshow('hsv',hsv)
    union= cv2.inRange(hsv, lower_blue, upper_blue)
    #cv2.imshow('blue',union)
    f1= cv2.erode(union, cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)), iterations=1)
    f2= cv2.erode(f1, cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)), iterations=1)
    object= cv2.moments(f2)
    if object['m00'] > 50000:
        cx= int(object['m10']/object['m00'])
        cy= int(object['m01']/object['m00'])
        cv2.circle(frame, (cx,cy), 10, (0,255,0), 2)
    cv2.imshow('rgb',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()