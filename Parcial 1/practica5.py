import cv2

img = cv2.imread('img1.jpg')
copia_img = img.copy()
roi = cv2.selectROI("Selecciona ROI", copia_img)
# Recortar la imagen usando las coordenadas del ROI
nuevaImagen = copia_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

alto, ancho, _ = nuevaImagen.shape
nuevaImagen = cv2.resize(nuevaImagen, (ancho, alto))
cv2.imwrite('img_ROI.jpg', nuevaImagen)

recorte = cv2.imread('img_ROI.jpg')
cv2.imshow('Recorte de la Imagen', recorte)
R,G,B = cv2.split(recorte)

while True:
    if cv2.waitKey(0) & 0xFF == ord('a'):
        print("Canal R, Tecla 'a' presionada")
        cv2.imshow('Canal R', R)
    if cv2.waitKey(0) & 0xFF == ord('s'):
        print("Canal G, Tecla 's' presionada")
        cv2.imshow('Canal G', G)
    if cv2.waitKey(0) & 0xFF == ord('d'):
        print("Canal B, Tecla 'd' presionada")
        cv2.imshow('Canal B', B)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        print("Saliendo del programa, Tecla 'q' presionada")
        break