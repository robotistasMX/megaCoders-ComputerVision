import cv2
img = cv2.imread("imagenes/img1.jpg")
img = cv2.resize(img,(360,480))
cv2.imshow("imagen",img)
cv2.waitKey(0)
cv2.destroyAllWindows()