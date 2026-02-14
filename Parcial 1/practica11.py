import cv2
import numpy as np

video = cv2.VideoCapture('video2.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
print(f"Frames por segundo: {fps}")
time = int(100 / fps)
while True:
    ret, frame = video.read()
    if ret == True:
        # ROJO (primer rango)
        rojo1 = np.array([0, 60, 50])
        rojo2 = np.array([10, 255, 255])
        

        # NARANJA (tercer y cuarto pin)
        naranja1 = np.array([11, 80, 80])
        naranja2 = np.array([25, 255, 255])
        kernel = np.ones((7,7),np.uint8)
        mask1 = cv2.inRange(frame, rojo1, rojo2)
        mask2 = cv2.inRange(frame, naranja1, naranja2)
        mask = cv2.add(mask1, mask2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        resultado = cv2.bitwise_and(frame, frame, mask=mask)
        resultado[mask > 0] = (10, 155, 25)

        cv2.namedWindow('Frame Original', cv2.WINDOW_NORMAL)
        cv2.imshow('Frame Original', resultado) 
        cv2.namedWindow('Video El Despertar', cv2.WINDOW_NORMAL)
        cv2.imshow('Video El Despertar', frame)
    if not ret:
        break
    if cv2.waitKey(time) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()