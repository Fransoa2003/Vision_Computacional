import cv2
import easygui as vent
import numpy as np

# funcion para obtener el contorno principal de una imagen
def ask_contorn(img):
    img = cv2.imread(img)
    img = cv2.resize(img, (600, 400))
    copy = img.copy()
    copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
    copy = cv2.GaussianBlur(copy, (7, 7), 0)
    _, valor = cv2.threshold(copy, 0, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 3), np.uint8)
    figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
    canyes = cv2.Canny(figura, 3, 3)
    contorno, _ = cv2.findContours(canyes, 
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
    if len(contorno) == 0:
        return None, img
    contorno_pincipal = max(contorno, key=cv2.contourArea)
    return contorno_pincipal, img
#Seleccion de imagenes y obtencion de contornos principales
imagen = vent.fileopenbox(msg="Selecciona una imagen",
                        title="Seleccionar imagen",
                        filetypes=["*.jpg", "*.png"],
                        default="")
contorno1, img1 = ask_contorn(imagen) # -> obtencion del contorno principal de la imagen 1
imagen2 = vent.fileopenbox(msg="Selecciona una imagen",
                        title="Seleccionar imagen",
                        filetypes=["*.jpg", "*.png"],
                        default="")
contorno2, img2 = ask_contorn(imagen2) # -> obtencion del contorno principal de la imagen 2

if contorno1 is None or contorno2 is None:
    similitud = cv2.matchShapes(contorno1, contorno2, cv2.CONTOURS_MATCH_I1, 0.0)
    print(f"Similitud entre las formas: {similitud}")
    print("No se encontraron contornos en una o ambas imágenes.")
    exit()
else:
    similitud = cv2.matchShapes(contorno1, contorno2, cv2.CONTOURS_MATCH_I1, 0.0)
    print(f"Similitud entre las formas: {similitud}")
    if similitud < 0.1:
        print("Las formas son similares.")
    else:
        print("Las formas no son similares.")

cv2.namedWindow('Imagen 1', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen 1', img1)

cv2.namedWindow('Imagen 2', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen 2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()