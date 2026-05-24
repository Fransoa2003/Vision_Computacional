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
texto = cv2.resize(texto, None, fx=2,fy=2, interpolation=cv2.INTER_CUBIC)
gris = cv2.cvtColor(texto, cv2.COLOR_BGR2GRAY)
gris = cv2.GaussianBlur(gris, (5,5), 0)
_, resp = cv2.threshold(gris, 150,255, cv2.THRESH_BINARY +cv2.THRESH_OTSU)

salida = pytesseract.image_to_string(resp, lang="eng")
print(salida)
hablar(salida)