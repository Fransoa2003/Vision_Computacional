from email import message
from tkinter import messagebox
import cv2
import easygui as vent

ib = False
ig = False
im = False
ie = False

imagen = vent.fileopenbox(msg="Selecciona una imagen",
                            title="Seleccionar imagen", 
                            filetypes=["*.jpg", "*.png"])
img = cv2.imread(imagen)
# Efecto Blur, sirve para suavizar la imagen, eliminando detalles y reduciendo el ruido. 
# El tamaño del kernel (15, 15) determina el grado de desenfoque aplicado a la imagen.
img_blur = cv2.blur(img, (15, 15))

# Filtro Gaussianblur, es un tipo de filtro de suavizado que utiliza una función gaussiana 
# para calcular el peso de cada píxel en la vecindad.
img_gaussian = cv2.GaussianBlur(img, (15, 15), 6)

#mediaBlur, es un filtro de suavizado que reemplaza cada píxel con la mediana de los píxeles vecinos.
img_median = cv2.medianBlur(img, 15)

#equalizeHist, es una técnica de procesamiento de imágenes que mejora el contraste de una imagen 
# al redistribuir los valores de intensidad de los píxeles.
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_equalized = cv2.equalizeHist(img_gray)


cv2.namedWindow('Imagen Original', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen Original', img)

# cv2.namedWindow('Imagen Blur', cv2.WINDOW_NORMAL)
# cv2.imshow('Imagen Blur', img_blur)

# cv2.namedWindow('Imagen Gaussian', cv2.WINDOW_NORMAL)
# cv2.imshow('Imagen Gaussian', img_gaussian)

# cv2.namedWindow('Imagen Median', cv2.WINDOW_NORMAL)
# cv2.imshow('Imagen Median', img_median)

# cv2.namedWindow('Imagen Gray', cv2.WINDOW_NORMAL)
# cv2.imshow('Imagen Gray', img_gray)

# cv2.namedWindow('Imagen Equalized', cv2.WINDOW_NORMAL)
# cv2.imshow('Imagen Equalized', img_equalized)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('b') and ib == False:
        archivo = vent.filesavebox(msg="Guardando imágenes...", 
                              title="Guardar", 
                              default="",
                              filetypes=["*.jpg", "*.png"])
        print("Guardando imagen Blur..."+archivo)
        if archivo is None:
            if not archivo.lower().endswith(('.jpg', '.png')):
                archivo += ".jpg"
            print("Archivo guardado como: " + archivo)
            cv2.imwrite(archivo, img_blur)
            ib = True
    elif cv2.waitKey(1) & 0xFF == ord('b') and ib == True:
        # messagebox.showerror("Error", "La imagen ya ha sido guardada.")
        vent.msgbox(msg="La imagen ya ha sido guardada.",
                    title="Error")
    if cv2.waitKey(1) & 0xFF == ord('g') and ig == False:
        archivo = vent.filesavebox(msg="Guardando imágenes...",
                                title="Guardar", 
                                default="",
                                filetypes=["*.jpg", "*.png"])
        cv2.imwrite(archivo, img_gaussian)
        ig = True
    elif cv2.waitKey(1) & 0xFF == ord('g') and ig == True:
        vent.msgbox(msg="La imagen ya ha sido guardada.",
                    title="Error")
    if cv2.waitKey(1) & 0xFF == ord('m') and im == False:
        archivo = vent.filesavebox(msg="Guardando imágenes...", 
                                title="Guardar", 
                                default="",
                                filetypes=["*.jpg", "*.png"])
        cv2.imwrite(archivo, img_median)
        im = True
    elif cv2.waitKey(1) & 0xFF == ord('m') and im == True:
        vent.msgbox(msg="La imagen ya ha sido guardada.",
                    title="Error")
    if cv2.waitKey(1) & 0xFF == ord('e') and ie == False:
        archivo = vent.filesavebox(msg="Guardando imágenes...",
                                title="Guardar", 
                                default="",
                                filetypes=["*.jpg", "*.png"])
        cv2.imwrite(archivo, img_equalized)
        ie = True
        print("Imágenes guardadas.")
    elif cv2.waitKey(1) & 0xFF == ord('e') and ie == True:
        vent.msgbox(msg="La imagen ya ha sido guardada.",
                    title="Error")
cv2.waitKey(0)
cv2.destroyAllWindows()