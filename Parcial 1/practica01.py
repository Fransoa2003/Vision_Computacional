import cv2
import easygui as ventana


extencion = ['*.jpg', '*.png', '*.jpeg']
imagen = ventana.fileopenbox(title='Selecciona una imagen', 
                          filetypes=extencion,
                          msg='Selecciona una imagen',
                          default='C:/')
print(imagen[len(imagen)-3:len(imagen)])
ext = imagen[len(imagen)-3:len(imagen)]

if ext in ['jpg', 'png', 'gif']:
    #renderizar una imagen y mostrar sus dimensiones
    img = cv2.imread(imagen)
    # Obtener dimensiones de la imagen
    alto, ancho = img.shape[:2]
    print(f'Image width: {ancho}')

    print(f'Image dimensions: {img.shape}')
    print(img)

    copia_img = img.copy()
    copia_img = cv2.resize(copia_img, (0, 0), fx=0.5, fy=0.5)
    cv2.namedWindow('Image_copy', cv2.WINDOW_NORMAL)
    cv2.imshow('Image_copy', copia_img)
    cv2.imwrite('img1_copy.jpg', copia_img)
    # Mostrar la imagen en una ventana redimensionable
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.imshow('Image', img)
    # Esperar hasta que se presione una tecla y cerrar la ventana
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("ERROR")