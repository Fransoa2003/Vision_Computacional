# colores rgb
# rojo claro: (255, 102, 102)
# rojo oscuro: (153, 0, 0)
# verde claro: (102, 255, 102)
# verde oscuro: (0, 153, 0)
# azul claro: (102, 102, 255)
# azul oscuro: (0, 0, 153)
# amarillo claro: (255, 255, 102)
# amarillo oscuro: (153, 153, 0)
# blanco: (255, 255, 255)
# blanco gris claro: (200, 200, 200)


import cv2
import numpy as np
img = cv2.imread('img1.jpg')
#Agregar texto
cv2.putText(img, #Imagen donde se pondrá el texto
            'Colores a cambiar', #Texto a agregar
            (250, 50), #Posición (x,y) donde se pondrá el texto
            cv2.FONT_HERSHEY_SIMPLEX, #Tipo de fuente
            1, #Tamaño de la fuente
            (0, 0, 255), #Color del texto en formato BGR
            2 #Grosor del texto
)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rojo1= np.array([0, 100, 100])
rojo2 = np.array([10, 255, 255])
rojo3 = np.array([160, 100, 100])
rojo4 = np.array([179, 255, 255])
kernel = np.ones((7,7),np.uint8)
mascara1 = cv2.inRange(hsv, rojo1, rojo2)
mascara2 = cv2.inRange(hsv, rojo3, rojo4)
mascara = cv2.add(mascara1, mascara2)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
resultado = cv2.bitwise_and(img, img, mask=mascara)
contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in contornos:
    area = cv2.contourArea(c)
    if area > 500:
        cv2.drawContours(resultado, [c], -1, (0, 0, 255), 1)
        areas = f'Area del contorno: {area}'
        x,y,h,w = cv2.boundingRect(c)
        cv2.putText(resultado, areas, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 100, 100), 1)
cv2.imshow('Imagen Original', img)
cv2.imshow('Imagen HSV', hsv)
cv2.imshow('Mascara', mascara)
cv2.imshow('Resultado', resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()