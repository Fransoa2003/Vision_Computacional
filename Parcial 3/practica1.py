import cv2
import pytesseract
import pyttsx3

def hablar(texto):
    voz = pyttsx3.init()
    voces = voz.getProperty('voices')
    voz.setProperty('voice', voces[0].id)
    voz.setProperty('rate', 150)
    voz.setProperty('volume', 1.0)
    voz.say(texto)
    voz.runAndWait()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

texto  = cv2.imread("texto2.png")
gris = cv2.cvtColor(texto, cv2.COLOR_BGR2GRAY)

salida = pytesseract.image_to_string(gris)
print(salida)
hablar(salida)