import cv2

img = cv2.imread('img1.jpg')
print(f"mitad ancho: {img.shape[1]//2}, mitad alto: {img.shape[0]//2}")
partirYP1 = img[0:, 0:475]
partirYP2 = img[0:, 475:]
partirXP1 = img[0:271, 0:]
partirXP2 = img[271:, 0:]
cv2.imwrite('parte.jpg', partirYP1)
cv2.imwrite('parte2.jpg', partirYP2)
cv2.imwrite('parteX.jpg', partirXP1)
cv2.imwrite('parteX2.jpg', partirXP2)
img_parteYP1 = cv2.imread('parte.jpg')
img_parteYP2 = cv2.imread("parte2.jpg")
img_parteXP1 = cv2.imread("parteX.jpg")
img_parteXP2 = cv2.imread("parteX2.jpg")

two_img_v = cv2.vconcat([img_parteXP1, img_parteXP2])
two_img_h = cv2.hconcat([img_parteYP2, img_parteYP1])



cv2.namedWindow('Imagenes Concatenadas', cv2.WINDOW_NORMAL)
cv2.imshow('Imagenes Concatenadas', two_img_v)
cv2.namedWindow('Imagenes Concatenadas Horizontal', cv2.WINDOW_NORMAL)
cv2.imshow('Imagenes Concatenadas Horizontal', two_img_h)

# cv2.namedWindow('Imagen Original', cv2.WINDOW_NORMAL)
# cv2.imshow('Imagen Original', img)
# cv2.namedWindow('Parte de la Imagen Y', cv2.WINDOW_NORMAL)
# cv2.imshow('Parte de la Imagen Y', img_parteY)
# cv2.namedWindow('Parte de la Imagen X', cv2.WINDOW_NORMAL)
# cv2.imshow('Parte de la Imagen X', img_parteX)

cv2.waitKey(0)
cv2.destroyAllWindows()