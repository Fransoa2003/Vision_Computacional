import cv2

img = cv2.imread('img1.jpg')
copia_img = img.copy()
copia_img = cv2.cvtColor(copia_img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(copia_img)
cv2.namedWindow('H', cv2.WINDOW_NORMAL)
cv2.imshow('H', h)
cv2.namedWindow('S', cv2.WINDOW_NORMAL)
cv2.imshow('S', s)
cv2.namedWindow('V', cv2.WINDOW_NORMAL)
cv2.imshow('V', v)
# Dividir la imagen en sus canales de color
# r,g,b = cv2.split(img)
# cv2.namedWindow('R', cv2.WINDOW_NORMAL)
# cv2.imshow('R', r)
# cv2.namedWindow('G', cv2.WINDOW_NORMAL)
# cv2.imshow('G', g)
# cv2.namedWindow('B', cv2.WINDOW_NORMAL)
# cv2.imshow('B', b)
# Obtener dimensiones de la imagen
# alto, ancho = img.shape[:2]
# print(f'Image width: {ancho}')
cv2.imwrite('img_H_copy.jpg', h)
cv2.imwrite('img_S_copy.jpg', s)
cv2.imwrite('img_V_copy.jpg', v)
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()