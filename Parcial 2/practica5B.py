import cv2
import easygui as vent
import numpy as np
import pyttsx3


voz = pyttsx3.init()
voces = voz.getProperty('voices')
voz.setProperty('voice', voces[0].id)
voz.setProperty('rate', 150)
voz.setProperty('volume', 1.0)

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

imagen = vent.fileopenbox(msg="Selecciona una imagen",
                        title="Seleccionar imagen",
                        filetypes=["*.jpg", "*.png"],
                        default="")
img, pr, d = extrar_carateristicas(imagen)
imagen2 = vent.fileopenbox(msg="Selecciona una imagen",
                        title="Seleccionar imagen",
                        filetypes=["*.jpg", "*.png"],
                        default="")
# img1 = cv2.imread(imagen)
img2, pr2, d2 = extrar_carateristicas(imagen2)
if img is None or img2 is None:
    print("No se pudieron cargar las imágenes.")
    exit()
else:
    similitud, carateristicas = comprar_imagenes(pr, d, pr2, d2)
    print(f"Puntos de referencia en imagen 1: {len(pr)}")
    print(f"Puntos de referencia en imagen 2: {len(pr2)}")
    print(f"Características comunes: {len(carateristicas)}")
    print(f"Similitud entre las imágenes: {similitud:.2f}")
    voz.say(f"La similitud entre las imágenes es de {similitud:.2f}")

    resultado = cv2.drawMatches(img, pr,
                                img2, pr2,
                                carateristicas,
                                None,
                                flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.putText(img, f"Puntos de referencia: {len(pr)}", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 100), 2)
    cv2.putText(img, f"Caracteristicas comunes: {len(carateristicas)}",
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 100), 2)
    cv2.putText(img, f"Similitud: {similitud:.2f}", 
                (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 100), 2)
    cv2.putText(img2, f"Puntos de referencia: {len(pr2)}", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 100), 2)
    cv2.putText(img2, f"Caracteristicas comunes: {len(carateristicas)}", 
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 100), 2)
    cv2.putText(img2, f"Similitud: {similitud:.2f}", 
                (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 100), 2)
    
    if similitud > 0.5:
        print("Las imágenes son similares.")
        cv2.putText(img, "Son similares", 
                    (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 0), 2)
        cv2.putText(img2, "Son similares", 
                    (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 0), 2)
        voz.say("Las imágenes son similares.")
        voz.runAndWait()
    else:
        print("Las imágenes no son similares.")
        cv2.putText(img, "No son similares", 
                    (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 200), 2)
        cv2.putText(img2, "No son similares", 
                    (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 200), 2)
        voz.say("Las imágenes no son similares.")
        voz.runAndWait()

cv2.namedWindow('Imagen 1', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen 1', img)

cv2.namedWindow('Imagen 2', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen 2', img2)

cv2.namedWindow('Resultado', cv2.WINDOW_NORMAL)
cv2.imshow('Resultado', resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()