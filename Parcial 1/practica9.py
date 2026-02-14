import cv2
import numpy as np
img = cv2.imread('colores_primarios.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
verde1= np.array([40, 25, 25])
verde2 = np.array([100, 255, 255])

azul1= np.array([100, 150, 0])
azul2 = np.array([140, 255, 255])
kernel = np.ones((7,7),np.uint8)

rojo1= np.array([0, 100, 100])
rojo2 = np.array([10, 255, 255])
# Azul
mascara_azul = cv2.inRange(hsv, azul1, azul2)
# verde
mascara = cv2.inRange(hsv, verde1, verde2)
# rojo
mascara_rojo = cv2.inRange(hsv, rojo1, rojo2)
# union de las mascaras
mascara = cv2.add(mascara, mascara_azul)
mascara = cv2.add(mascara, mascara_rojo)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)

resultado = cv2.bitwise_and(img, img, mask=mascara)
resultado[mascara > 0] = (255, 255, 255)

alpha = 0.9 # Peso de la primera imagen
beta = 0.9 # Peso de la segunda imagen
gamma = 0 # Valor escalar añadido a cada suma

union = cv2.addWeighted(img, alpha, resultado, beta, gamma)

cv2.imshow('Imagen Original', img)
cv2.imshow('Imagen HSV', hsv)
cv2.imshow('Resultado', resultado)
cv2.imshow('Union', union)
cv2.waitKey(0)
cv2.destroyAllWindows()