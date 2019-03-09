#Librerias necesarias
import cv2
import numpy as np

maxCirculos=6
maxCirculos=maxCirculos-1

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    framegrey1 = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow("Original", framegrey1)
    
    
    gray = cv2.GaussianBlur(framegrey1, (1,1), 2)
    """
    La funcion cv2.medianBlur toma la mediana de todos los pixeles bajo el area del kernel y el elemento central se sustituye por este valor mediano. 
    Esto es muy eficaz contra el ruido en las imagenes.
    Lo interesante es que el elemento central es un valor recien calculado que puede ser un valor de pixel en la imagen o un nuevo valor.
    Pero en el desenfoque mediano, el elemento central siempre es reemplazado por algun valor de pixel en la imagen.
    Reduce el ruido de manera efectiva. Su tamano de nucleo debe ser un numero entero impar positivo.
    """
    
    gray = cv2.medianBlur(gray,5)

    # La funcion transforma la imagen en escala de grises a una imagen binaria
    gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,19,3)
    
    #Se crea el kernel que se utilizara para la funcion erode y dilate
    kernel = np.ones((3,3),np.uint8)
    
	  #Erosion quita la estructura de pixeles de la capa mas externa
	  #Dilation agrega pixeles a la estructura de la capa mas externa
    gray = cv2.erode(gray,kernel,iterations = 1) 
    gray = cv2.dilate(gray,kernel,iterations = 1)
    
    #DETECCION DE CIRCULOS
    circles =  cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 25, 5, 100)
    
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