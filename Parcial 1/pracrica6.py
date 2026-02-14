# import cv2
# img = cv2.imread('img1.jpg')
# img2 = cv2.imread('img1_copy.jpg')

# alto1, ancho1, _ = img.shape
# alto2, ancho2, _ = img2.shape

# if (alto1 + ancho1) > (alto2 + ancho2):
#     print("La imagen 1 es más grande")
#     img_resized = cv2.resize(img, (ancho2, alto2))
# else:
#     print("La imagen 2 es más grande")
#     img2_resized = cv2.resize(img2, (ancho1, alto1))

# alpha = 0.9 # Peso de la primera imagen
# beta = 0.1  # Peso de la segunda imagen
# gamma = 0  # Valor escalar añadido a cada suma

# resultado = cv2.addWeighted(img, alpha, img2, beta, gamma)
# cv2.imwrite('imagen_fusionada.jpg', resultado)
# cv2.imshow('Imagen Fusionada', resultado)

# cv2.imshow('Imagen 1', img)
# cv2.imshow('Imagen 2', img2)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2

img = cv2.imread('img_con_fondo.jpg')
img2 = cv2.imread('img_sin_fondo.png')

if img is None or img2 is None:
    print("Error: No se pudo cargar una de las imágenes")
    exit()

alto1, ancho1, _ = img.shape
alto2, ancho2, _ = img2.shape

# Comparar áreas (mejor que alto + ancho)
area1 = alto1 * ancho1
area2 = alto2 * ancho2

if area1 > area2:
    print("La imagen 1 es más grande")
    img = cv2.resize(img, (ancho2, alto2))
else:
    print("La imagen 2 es más grande")
    img2 = cv2.resize(img2, (ancho1, alto1))

# 🔥 AQUÍ ya tienen el mismo tamaño, garantizado
alpha = 0.5
beta = 0.5
gamma = 0

resultado = cv2.addWeighted(img, alpha, img2, beta, gamma)

cv2.imshow('Imagen Fusionada', resultado)
cv2.imshow('Imagen 1', img)
cv2.imshow('Imagen 2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
