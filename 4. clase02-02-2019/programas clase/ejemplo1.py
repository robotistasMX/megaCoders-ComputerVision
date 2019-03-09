import numpy as numpy
import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascades/haarcascade_eye.xml')
smile = cv.CascadeClassifier('haarcascades/haarcascade_smile.xml')
cap = cv.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h), (0,255,0), 2)
        gray2 = gray[y:y+h, x:x+w]
        color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(gray2)
        smiles =smile.detectMultiScale(gray2)
        for(x,y,w,h) in eyes:
            cv.rectangle(color,(x,y),(x+w,y+h), (0,0,255), 2)
        for(x,y,w,h) in smiles:
            cv.rectangle(color,(x,y),(x+w,y+h), (255,0,0), 2)
    cv.imshow('frame', frame)
    #cv.imshow('cara', color)
    if cv.waitKey(10) == 27:
        break 

cap.release()
cv.destroyAllWindows()
