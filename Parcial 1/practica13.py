import cv2
import numpy as np
import imutils 
from datetime import datetime
camara = cv2.VideoCapture("video2.mp4")
camara.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camara.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while (True):
    f, frame = camara.read()
    if f == False:
        break
    else:
        tiempo = datetime.now()
        frame = imutils.resize(frame, width=640)
        frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # rojo
        rojo1 = np.array([0, 60, 50])
        rojo2 = np.array([10, 255, 255])
        rojo3 = np.array([170, 60, 50])
        rojo4 = np.array([180, 255, 255])
        # negro
        negro1 = np.array([0, 0, 0])
        negro2 = np.array([180, 255, 50])
        mask1 = cv2.inRange(hsv, rojo1, rojo2)
        mask2 = cv2.inRange(hsv, rojo3, rojo4)
        mask3 = cv2.inRange(hsv, negro1, negro2)
        mask = cv2.add(mask1, mask2)
        mask = cv2.add(mask, mask3)
        kernel = np.ones((7,7),np.uint8)

        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        resultado = cv2.bitwise_and(frame, frame, mask=mask)
        # resultado[mask > 0] = (10, 155, 25)
        frame_gris = cv2.cvtColor(frame_gris, cv2.COLOR_GRAY2BGR)
        frame_gris = cv2.add(frame_gris, resultado)
        frame = cv2.add(frame, resultado)


        cv2.namedWindow('Camara', cv2.WINDOW_NORMAL)
        cv2.imshow('Camara', frame)
        cv2.namedWindow('Camara Gris', cv2.WINDOW_NORMAL)
        # cv2.imshow('Camara Resultado', resultado)
        cv2.imshow('Camara Gris', frame_gris)
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            nombre = "archivo"+str(tiempo.second)+".jpg"
            cv2.imwrite(nombre, frame_gris)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

camara.release()
cv2.destroyAllWindows()