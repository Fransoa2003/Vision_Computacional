import cv2
import easygui as vent
import numpy as np
import datetime as dt
import pyttsx3

voz = pyttsx3.init()
voces = voz.getProperty('voices')
voz.setProperty('voice', voces[0].id)
voz.setProperty('rate', 150)
voz.setProperty('volume', 1.0)
segundo = dt.datetime.now().second
print(segundo)

camara = cv2.VideoCapture(0)
salida = cv2.VideoWriter(f'salida{segundo}.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))
voz.say("La cámara se ha iniciado. Presiona la tecla 'q' para detener la grabación.")
voz.runAndWait()



while (camara.isOpened()):
    ret, frame = camara.read()
    if ret:
        frame = cv2.flip(frame, 1)
        
        cv2.imshow("Camara", frame)
        salida.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            voz.say("La grabación se ha detenido.")
            detner = True
            break
    else:
        break
camara.release()
salida.release()
cv2.destroyAllWindows()

if detner:
    voz.say("La cámara se ha detenido.")
    voz.runAndWait()
    