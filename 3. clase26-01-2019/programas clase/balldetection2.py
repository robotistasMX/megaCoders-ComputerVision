import cv2
import numpy as np

maxCirculos=6
maxCirculos=maxCirculos-1

lower = np.array([0,0,66])
upper = np.array([162,114,255])

video = cv2.VideoCapture(1)

while True:
    ret, frame = video.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask= cv2.inRange(hsv, lower, upper)

    gray = cv2.adaptiveThreshold(mask,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,19,3)

    #Se crea el kernel que se utilizara para la funcion erode y dilate
    kernel = np.ones((3,3),np.uint8)

	  #Erosion quita la estructura de pixeles de la capa mas externa
	  #Dilation agrega pixeles a la estructura de la capa mas externa


    gray = cv2.erode(gray,kernel,iterations = 1)
    gray = cv2.dilate(gray,kernel,iterations = 1)

    #DETECCION DE CIRCULOS
    circles =  cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 28, 5, 100)

    #DIBUJAMOS LOS CIRCULOS EN LOS ENCONTRADOS EN FRAME
    #DIBUJARA SOLAMENTE EL MAXIMO DE CIRCULOS PERMITIDO
    circulos=0
    if circles is not None:
        try:
            for c in circles[0]:
                cv2.circle(frame, (c[0],c[1]), c[2], (0,255,0),2)
                circulos=circulos+1
                print("Coordenada X: " + str(c[0]))
                print("Coordenada Y: " + str(c[1]))
                if(circulos>maxCirculos):
                    break
        except:
            print("NO SE DETECTA EL BALON")
    else:
        print("NO SE DETECTA EL BALON")

    cv2.imshow("video", frame)
    cv2.imshow("filtros", gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()