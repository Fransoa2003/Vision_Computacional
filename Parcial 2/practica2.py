import cv2
import easygui as vent
import numpy as np

imagen = vent.fileopenbox(msg="Selecciona una imagen",
                            title="Seleccionar imagen",
                            filetypes=["*.jpg", "*.png"])
img = cv2.imread(imagen)
copy = img.copy()
copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
copy = cv2.GaussianBlur(copy, (5, 5), 0)
_, valor = cv2.threshold(copy, 190, 255, cv2.THRESH_BINARY)
kernel = np.ones((3, 3), np.uint8)
figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
bordes = cv2.Canny(figura, 3, 3)
contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, 
                 contornos, 
                 -1, 
                 (0, 255, 0), 
                 2)
lista = []
for i in range(len(contornos)):
    area = cv2.contourArea(contornos[i])
    # print("Área del contorno {}: {}".format(i, area))
    if area > 1000:
        lista.append(area)
        print("Área del contorno {}: {}".format(i, area))
        print(f"los objetos encontrados son: {len(lista)}")

cv2.namedWindow('Imagen Original', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen Original', img)
cv2.namedWindow('Imagen Copia', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen Copia', copy)
cv2.namedWindow('Imagen canny', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen canny', bordes)

cv2.waitKey(0)
cv2.destroyAllWindows()