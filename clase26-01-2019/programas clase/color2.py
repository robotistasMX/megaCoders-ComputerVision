import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)

def nothing(x):
    pass

#Creamos una ventana llamada 'image' en la que habra todos los sliders
cv2.namedWindow('image')
cv2.createTrackbar('B Minimo','image',0,255,nothing)
cv2.createTrackbar('B Maximo','image',0,255,nothing)
cv2.createTrackbar('G Minimo','image',0,255,nothing)
cv2.createTrackbar('G Maximo','image',0,255,nothing)
cv2.createTrackbar('R Minimo','image',0,255,nothing)
cv2.createTrackbar('R Maximo','image',0,255,nothing)
 
while(1):
  _,frame = cap.read() #Leer un frame
  
  #Los valores maximo y minimo de H,S y V se guardan en funcion de la posicion de los sliders
  bMin = cv2.getTrackbarPos('B Minimo','image')
  bMax = cv2.getTrackbarPos('B Maximo','image')
  gMin = cv2.getTrackbarPos('G Minimo','image')
  gMax = cv2.getTrackbarPos('G Maximo','image')
  rMin = cv2.getTrackbarPos('R Minimo','image')
  rMax = cv2.getTrackbarPos('R Maximo','image')
 
  #Se crea un array con las posiciones minimas y maximas
  lower=np.array([bMin,gMin,rMin])
  upper=np.array([bMax,gMax,rMax])
 
  #Deteccion de colores
  mask = cv2.inRange(frame, lower, upper)
 
  #Mostrar los resultados y salir
  cv2.imshow('camara',frame)
  cv2.imshow('mask',mask)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()