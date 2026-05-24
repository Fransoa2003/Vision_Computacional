import cv2
import easyocr
import pyttsx3



lenguaje = easyocr.Reader(['es'])
resultado  = lenguaje.readtext("texto2.png")

for (p1, texto, p2) in resultado:
    print(texto)