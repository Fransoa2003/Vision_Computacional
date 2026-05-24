import cv2
import easygui as vent
import numpy as np

# Detencion de objetos mediante su centro
imagen = vent.fileopenbox(msg="Selecciona una imagen",
                            title="Seleccionar imagen",
                            filetypes=["*.jpg", "*.png"],
                            default="")
img = cv2.imread(imagen)
img = cv2.resize(img, (600, 400))
copy = img.copy()
copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
copy = cv2.GaussianBlur(copy, (7, 7), 0)
_, valor = cv2.threshold(copy, 70, 90, cv2.THRESH_BINARY)
kernel = np.ones((5, 3), np.uint8)
figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
bordes = cv2.Canny(figura, 3, 3)
contornos, _ = cv2.findContours(bordes, 
                                cv2.RETR_EXTERNAL, 
                                cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, 
                 contornos, 
                 -1, 
                 (0, 255, 0), 
                 2)
lista = []

for i in range(len(contornos)):
    area = cv2.contourArea(contornos[i])
    if area > 700:
        lista.append(area)
        M = cv2.moments(contornos[i])
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(img, (cX, cY), 5, (255, 0, 0), -1)
            print(f"Centro del contorno {i}: ({cX}, {cY})")
            img = cv2.putText(img, f"({cX}, {cY})", (cX - 20, cY - 20), 
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

cv2.putText(img, f"Los objetos encontrados son: {len(lista)}", (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.namedWindow('Imagen Original', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen Original', img)
cv2.namedWindow('Imagen Copia', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen Copia', figura)

cv2.waitKey(0)
cv2.destroyAllWindows()