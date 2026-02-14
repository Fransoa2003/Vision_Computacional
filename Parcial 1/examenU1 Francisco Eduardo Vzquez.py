import cv2
import numpy as np
import imutils 
import imutils 
from datetime import datetime


video = cv2.VideoCapture("Super Mario Galaxy_ Trailer.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
print(f"Frames por segundo: {fps}")
# time = int(10 / fps)
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
while True:
    ret, frame = video.read()
    if not ret:
        break
    else:
        # tiempo = datetime.now()
        frame = imutils.resize(frame, width=640)
        frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow('Video', frame)
        cv2.imshow('Video Gris', frame_gris)
        # Parte 1 ------------------------------------------------------------------------------
        if cv2.waitKey(1) & 0xFF == ord('s'):
            nombre = "marioyluigi"+".jpg"
            cv2.imwrite(nombre, frame)
        if cv2.waitKey(1) & 0xFF == ord('d'):
            nombre = "logonintendo"+".jpg"
            cv2.imwrite(nombre, frame)
        if cv2.waitKey(1) & 0xFF == ord('f'):
            nombre = "yoshi"+".jpg"
            cv2.imwrite(nombre, frame)
        # if tiempo.second == 8:
        #     nombre = "Mariomarioyluigi"+str(tiempo.second)+".jpg"
        #     cv2.imwrite(nombre, frame)
        #     print("Imagen guardada")
        #     break
        # Parte 1 ------------------------------------------------------------------------------

        # Parte 2 ------------------------------------------------------------------------------
        img1 = cv2.imread('marioyluigi.jpg')
        img2 = cv2.imread('marioyluigi.jpg')
        img3 = cv2.imread('logonintendo.jpg')
        img4 = cv2.imread('yoshi.jpg')
        
        copia_img = cv2.cvtColor(copia_img, cv2.COLOR_BGR2HSV)
        hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
        hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
        hsv3 = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
        hsv4 = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV)

        #rojo
        rojo1= np.array([0, 100, 100])
        rojo2 = np.array([10, 255, 255])

        #verde
        verde_bajo = np.array([40, 60, 50])
        verde_fuerte = np.array([80, 255, 255])
        kernel = np.ones((7,7),np.uint8)

        mask1 = cv2.inRange(hsv, rojo1, rojo2)
        mask2 = cv2.inRange(hsv2, verde_bajo, verde_fuerte)
        mask3 = cv2.inRange(hsv3, rojo1, rojo2)
        mask4 = cv2.inRange(hsv4, verde_bajo, verde_fuerte)
        mask_1 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernel)
        mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_OPEN, kernel)
        mask_2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel)
        mask_2 = cv2.morphologyEx(mask_2, cv2.MORPH_CLOSE, kernel)
        mask_3 = cv2.morphologyEx(mask3, cv2.MORPH_OPEN, kernel)
        mask_4 = cv2.morphologyEx(mask4, cv2.MORPH_OPEN, kernel)
        mask_4 = cv2.morphologyEx(mask_4, cv2.MORPH_CLOSE, kernel)
        resultado1 = cv2.bitwise_and(img1, img1, mask=mask_1)
        resultado2 = cv2.bitwise_and(img2, img2, mask=mask_2)
        resultado3 = cv2.bitwise_and(img3, img3, mask=mask_3)
        resultado4 = cv2.bitwise_and(img4, img4, mask=mask_4)
        # cv2.imshow('Resultado', resultado)
        # rojo = (10, 255, 255)
        resultado1[mask_1 > 0] = (0, 100, 10)
        resultado2[mask_2 > 0] = (40, 10, 100)
        resultado3[mask_3 > 0] = (40, 10, 100)
        resultado4[mask_4 > 0] = (110, 120, 20)
        # Parte 2 ------------------------------------------------------------------------------

        # parte 3 ------------------------------------------------------------------------------
        copia_img = img4.copy()
        h,s,v = cv2.split(copia_img)
        cv2.imshow('H canal', h)
        cv2.imshow('S canal', s)    
        cv2.imshow('V canal', v)
        three_img_h = cv2.hconcat([h, s, v])
        cv2.imshow('Canales HSV concatenados', three_img_h)
        cv2.imwrite('cacacambiocolor.jpg', three_img_h)
        # Parte 3 ------------------------------------------------------------------------------

        # Parte 2 ------------------------------------------------------------------------------
        cv2.imshow('Resultado Mario', resultado1)
        cv2.imshow('Resultado lugi', resultado2)
        cv2.imshow('Resultado Nintendo', resultado3)
        cv2.imshow('Resultado Yoshi', resultado4)
        cv2.imwrite('Mariocambiodecolor1.jpg', resultado1)
        cv2.imwrite('lugicambiodecolor1.jpg', resultado2)
        cv2.imwrite('nintendocambiodecolor1.jpg', resultado3)
        cv2.imwrite('yoshicambiodecolor1.jpg', resultado4)
        # parte 2 ------------------------------------------------------------------------------
        # parte 4 ------------------------------------------------------------------------------
        copia_img = img4.copy()
        roi = cv2.selectROI("Selecciona ROI", copia_img)
        nuevaImagen = copia_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()