import cv2
import easygui as vent
import numpy as np
import pyttsx3

def extrar_carateristicas(img):
    img1 = cv2.imread(img)
    im1 = cv2.resize(img1, (600, 600))
    copy = im1.copy()
    copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create(nfeatures=150)
    pr, d = sift.detectAndCompute(copy, None)
    return im1, pr, d

def comprar_imagenes(pr1, d1, pr2, d2):
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(d1,d2, k=2)
    carateristicas = []
    for a in matches:
        if len(a) == 2:
            m, n = a
            if m.distance < 0.75 * n.distance:
                carateristicas.append(m)
    if max(len(pr1), len(pr2)) > 0:
        similitud = len(carateristicas) / min(len(pr1), len(pr2))
    else:
        similitud = 0
    return similitud, carateristicas

def contor(img):
    copy = img.copy()
    copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
    copy = cv2.GaussianBlur(copy, (5, 5), 0)
    _, valor = cv2.threshold(copy, 218, 220, cv2.THRESH_BINARY )
    kernel = np.ones((5, 3), np.uint8)
    figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
    bordes = cv2.Canny(figura, 3, 3)
    contornos, _ = cv2.findContours(bordes, 
                                cv2.RETR_EXTERNAL, 
                                cv2.CHAIN_APPROX_SIMPLE)
    return contornos, figura, copy

def cantidad(cantidad):
    voz = pyttsx3.init()
    voces = voz.getProperty('voices')
    voz.setProperty('voice', voces[0].id)
    voz.setProperty('rate', 150)
    voz.setProperty('volume', 1.0)

    voz.say(f"Se analizaron {cantidad} piezas correctamente")
    voz.runAndWait()


#Parte 1
def inicio():
    voz = pyttsx3.init()
    voces = voz.getProperty('voices')
    voz.setProperty('voice', voces[0].id)
    voz.setProperty('rate', 150)
    voz.setProperty('volume', 1.0)

    voz.say("Alumno Francisco Eduardo Vazquez Carvajal iniciando análisis de imagen")
    voz.runAndWait()

inicio()

img = cv2.imread('examenIntento2.jpg')
contorno, figura, GaussianBlur = contor(img)
copy_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.drawContours(img, 
                 contorno, 
                 -1, 
                 (0, 255, 0), 
                 2)
lista = []

for i in range(len(contorno)):
    area = cv2.contourArea(contorno[i])
    if area > 1200:
        lista.append(area)
        M = cv2.moments(contorno[i])
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(img, (cX, cY), 5, (255, 0, 0), -1)
            print(f"Centro del contorno {i}: ({cX}, {cY})")
            img = cv2.putText(img, f"({cX}, {cY})", (cX - 20, cY - 20), 
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)

cv2.putText(img, f"Los objetos encontrados son: {len(lista)}", (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 50, 100), 3)

#ROI
copia_img = img.copy()
roi = cv2.selectROI("Selecciona ROI", copia_img)
# Recortar la imagen usando las coordenadas del ROI
nuevaImagen = copia_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

alto, ancho, _ = nuevaImagen.shape
nuevaImagen = cv2.resize(nuevaImagen, (ancho, alto))
cv2.imwrite('imgR1.jpg', nuevaImagen)
cv2.destroyAllWindows()

roi = cv2.selectROI("Selecciona ROI", copia_img)
nuevaImagen2 = copia_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
alto, ancho, _ = nuevaImagen.shape
nuevaImagen = cv2.resize(nuevaImagen, (ancho, alto))
cv2.imwrite('imgR2.jpg', nuevaImagen2)

roi = cv2.selectROI("Selecciona ROI", copia_img)
nuevaImagen3 = copia_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
alto, ancho, _ = nuevaImagen.shape
nuevaImagen = cv2.resize(nuevaImagen, (ancho, alto))
cv2.imwrite('imgR3.jpg', nuevaImagen3)

roi = cv2.selectROI("Selecciona ROI", copia_img)
nuevaImagen4 = copia_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
alto, ancho, _ = nuevaImagen.shape
nuevaImagen = cv2.resize(nuevaImagen, (ancho, alto))
cv2.imwrite('imgR4.jpg', nuevaImagen4)

roi = cv2.selectROI("Selecciona ROI", copia_img)
nuevaImagen5 = copia_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
alto, ancho, _ = nuevaImagen.shape
nuevaImagen = cv2.resize(nuevaImagen, (ancho, alto))
cv2.imwrite('imgR5.jpg', nuevaImagen5)

roi = cv2.selectROI("Selecciona ROI", copia_img)
nuevaImagen6 = copia_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
alto, ancho, _ = nuevaImagen.shape
nuevaImagen = cv2.resize(nuevaImagen, (ancho, alto))
cv2.imwrite('imgR6.jpg', nuevaImagen6)

roi = cv2.selectROI("Selecciona ROI", copia_img)
nuevaImagen7 = copia_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
alto, ancho, _ = nuevaImagen.shape
nuevaImagen = cv2.resize(nuevaImagen, (ancho, alto))
cv2.imwrite('imgR7.jpg', nuevaImagen7)


recorte1 = cv2.imread('imgR1.jpg')
cv2.imshow('Recorte1', recorte1)
recorte2 = cv2.imread('imgR2.jpg')
cv2.imshow('Recorte2', recorte2)
recorte3 = cv2.imread('imgR3.jpg')
cv2.imshow('Recorte3', recorte3)
recorte4 = cv2.imread('imgR4.jpg')
cv2.imshow('Recorte4', recorte4)
recorte5 = cv2.imread('imgR5.jpg')
cv2.imshow('Recorte5', recorte5)
recorte6 = cv2.imread('imgR6.jpg')
cv2.imshow('Recorte6', recorte6)
recorte7 = cv2.imread('imgR7.jpg')
cv2.imshow('Recorte7', recorte7)



cv2.namedWindow('Imagen Original', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen Original', img)

cv2.namedWindow('imagen binaria', cv2.WINDOW_NORMAL)
cv2.imshow('imagen binaria', figura)

cv2.namedWindow('Gaussiano', cv2.WINDOW_NORMAL)
cv2.imshow('Gaussiano', GaussianBlur)

cv2.namedWindow('Escala de grises', cv2.WINDOW_NORMAL)
cv2.imshow('Escala de grises', copy_gris)

while True:
    key = cv2.waitKey() & 0xFF
    if key == ord('q'):
        break
    if key == ord("s"):
        nombre = f"Imagen_Guardada.jpg"
        cv2.imwrite(nombre, img)
    if key == ord("v"):
        cantidad(len(lista))
cv2.waitKey(0)
cv2.destroyAllWindows()