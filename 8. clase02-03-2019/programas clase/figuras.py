import cv2
import numpy as np

cap = cv2.VideoCapture(1)
font= cv2.FONT_HERSHEY_PLAIN
#0 10 134 255 0 255

def nothing(x):
    pass



#Creamos una ventana llamada 'image' en la que habra todos los sliders
cv2.namedWindow('image')
cv2.createTrackbar('Hue Minimo','image',0,255,nothing)
cv2.createTrackbar('Hue Maximo','image',0,255,nothing)
cv2.createTrackbar('Saturation Minimo','image',0,255,nothing)
cv2.createTrackbar('Saturation Maximo','image',0,255,nothing)
cv2.createTrackbar('Value Minimo','image',0,255,nothing)
cv2.createTrackbar('Value Maximo','image',0,255,nothing)

while(1):
  _,frame = cap.read() #Leer un frame
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Convertirlo a espacio de color HSV

  #Los valores maximo y minimo de H,S y V se guardan en funcion de la posicion de los sliders
  hMin = cv2.getTrackbarPos('Hue Minimo','image')
  hMax = cv2.getTrackbarPos('Hue Maximo','image')
  sMin = cv2.getTrackbarPos('Saturation Minimo','image')
  sMax = cv2.getTrackbarPos('Saturation Maximo','image')
  vMin = cv2.getTrackbarPos('Value Minimo','image')
  vMax = cv2.getTrackbarPos('Value Maximo','image')

  #Se crea un array con las posiciones minimas y maximas
  lower=np.array([hMin,sMin,vMin])
  upper=np.array([hMax,sMax,vMax])

  #Deteccion de colores
  mask = cv2.inRange(hsv, lower, upper)
  #Detectar figuras
  kernel= np.ones((5,5), np.uint8)
  mask= cv2.erode(mask,kernel)

  _, contours, _ =cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  for cnt in contours:
      area= cv2.contourArea(cnt)
      aprox= cv2.approxPolyDP(cnt, 0.012*cv2.arcLength(cnt, True), True)
      x= aprox.ravel()[0]
      y= aprox.ravel()[1]
      if area > 400:
          cv2.drawContours(frame, [aprox], 0, (0,0,0), 5)
          object= cv2.moments(area)
          cx= int(object['m10']/object['m00'])
          cy= int(object['m01']/object['m00'])
          cv2.circle(frame, (cx,cy), 10, (0,255,0), 2)
          if len(aprox)==4:
              cv2.putText(frame, "RECTANGULO", (x,y), font, 1, (0,255,0))
          if len(aprox)==3:
              cv2.putText(frame, "TRIANGULO", (x,y), font, 1, (0,255,0))
          if len(aprox)==5:
              cv2.putText(frame, "PENTAGONO", (x,y), font, 1, (0,255,0))
          if len(aprox)==6:
              cv2.putText(frame, "HEXAGONO", (x,y), font, 1, (0,255,0))
          if len(aprox)==7:
              cv2.putText(frame, "HEPTAGONO", (x,y), font, 1, (0,255,0))
          if len(aprox)==8:
              cv2.putText(frame, "OCTAGONO", (x,y), font, 1, (0,255,0))
          if len(aprox)==7:
              cv2.putText(frame, "HEPTAGONO", (x,y), font, 1, (0,255,0))
          if len(aprox)==8:
              cv2.putText(frame, "OCTAGONO", (x,y), font, 1, (0,255,0))
          if len(aprox)==9:
              cv2.putText(frame, "ENEAGONO", (x,y), font, 1, (0,255,0))
          if len(aprox)==10:
              cv2.putText(frame, "DECAGONO", (x,y), font, 1, (0,255,0))
          if len(aprox)>11:
              cv2.putText(frame, "CIRCULO", (x,y), font, 1, (0,255,0))


  #Mostrar los resultados y salir
  cv2.imshow('frame',frame)
  cv2.imshow('binary',mask)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
