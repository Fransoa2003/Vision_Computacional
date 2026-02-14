import cv2

img = cv2.imread('img1.jpg')
copia_img = img.copy()
copia_img = cv2.cvtColor(copia_img, cv2.COLOR_BGR2GRAY)
# concatenacion de imagenes vertical
two_img_v = cv2.vconcat([img, cv2.cvtColor(copia_img, cv2.COLOR_GRAY2BGR)])
# concatenacion de imagenes horizontal
two_img_h = cv2.hconcat([img, cv2.cvtColor(copia_img, cv2.COLOR_GRAY2BGR)])

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', two_img_v)
cv2.namedWindow('Image2', cv2.WINDOW_NORMAL)
cv2.imshow('Image2', two_img_h)
# cv2.namedWindow('GRIS', cv2.WINDOW_NORMAL)
# cv2.imshow('GRIS', copia_img)


cv2.waitKey(0)
cv2.destroyAllWindows()