import cv2
import numpy as np
import imutils 

img = cv2.imread('mario.jpeg')
copia_img = img.copy()
copia_img = cv2.cvtColor(copia_img, cv2.COLOR_BGR2HSV)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rojo1= np.array([0, 100, 100])
rojo2 = np.array([10, 255, 255])

verde1 = np.array([40, 100, 100])
verde2 = np.array([80, 255, 255])

azul1 = np.array([100, 100, 100])
azul2 = np.array([140, 255, 255])

kernel = np.ones((7,7),np.uint8)
mascara1 = cv2.inRange(hsv, rojo1, rojo2)
mascara2 = cv2.inRange(hsv, verde1, verde2)
mascara3 = cv2.inRange(hsv, azul1, azul2)

mascara = cv2.add(mascara1, mascara2)
mascara = cv2.add(mascara, mascara3)

mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
resultado = cv2.bitwise_and(img, img, mask=mascara)
contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#muestras si hay color rojo, verde o azul con un terxto estatico en la parte superior de la imagen
if cv2.countNonZero(mascara1) > 0:
    cv2.putText(resultado, 'Contiene color Rojo', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
if cv2.countNonZero(mascara2) > 0:
    cv2.putText(resultado, 'Contiene color Verde', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
if cv2.countNonZero(mascara3) > 0:
    cv2.putText(resultado, 'Contiene color Azul', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.imshow('original', img)
cv2.namedWindow('Resultado', cv2.WINDOW_NORMAL)
cv2.imshow('Resultado', resultado)
for c in contornos:
    area = cv2.contourArea(c)
    if area > 500:
        cv2.drawContours(resultado, [c], -1, (0, 0, 255), 1)
        areas = f'Area del contorno: {area}'
        x,y,h,w = cv2.boundingRect(c)
        cv2.putText(resultado, areas, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 100, 100), 1)

while True:
    if cv2.waitKey(0) & 0xFF == ord('c'):
        #conatenamos los canales HSV horizontalmente
        h,s,v = cv2.split(copia_img)

        cv2.putText(h,'Canal H', (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(s,'Canal S', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(v,'Canal V', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        three_img_h = cv2.hconcat([h, s, v])



        # cv2.namedWindow('Canales HSV concatenados', cv2.WINDOW_NORMAL)
        # cv2.imshow('Canales HSV concatenados', three_img_h)
        #conestamos los canales RGB horizontalmente
        b,g,r = cv2.split(img)
        cv2.putText(b,'Canal B', (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(g,'Canal G', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(r,'Canal R', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        three_img_h_rgb = cv2.hconcat([b, g, r])
        # cv2.namedWindow('Canales RGB concatenados', cv2.WINDOW_NORMAL)
        # cv2.imshow('Canales RGB concatenados', three_img_h_rgb)

        #Concarenamos ambas imagenes verticalmente
        final_concat = cv2.vconcat([three_img_h, three_img_h_rgb])
        cv2.namedWindow('Concatenacion Final', cv2.WINDOW_NORMAL)
        cv2.imshow('Concatenacion Final', final_concat)

        cv2.imwrite('img_concatenada.jpg', final_concat)
    

        
    if cv2.waitKey(0) & 0xFF == ord('q'):
        print("Saliendo...")
        break


cv2.waitKey(0)
cv2.destroyAllWindows()