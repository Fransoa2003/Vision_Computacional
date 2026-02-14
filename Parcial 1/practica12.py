import cv2
import numpy as np
camara = cv2.VideoCapture(0)
while (camara.isOpened()):
    f, frame = camara.read()
    if f == True:
        frame = cv2.flip(frame, 1)
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
        resultado[mask > 0] = (10, 155, 25)
        cv2.imshow('Resultado', resultado)
        cv2.imshow('Camara', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()