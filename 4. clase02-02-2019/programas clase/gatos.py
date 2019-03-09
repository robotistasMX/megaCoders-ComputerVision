import cv2
import numpy as np 

cat = cv2.CascadeClassifier('haarcascades/haarcascade_frontalcatface_extended.xml')

frame = cv2.imread("img/cat3.jpg")

gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
cats = cat.detectMultiScale(gray)
for (i, (x,y,w,h)) in enumerate(cats):  
    cv2.rectangle(frame,(x,y), (x+w,y+h),(0,0,255),2)
    cv2.putText(frame, "Gatito #{}".format(i+1), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0,0,255),2)

cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()