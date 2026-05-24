import cv2
import easygui as vent
import numpy as np
def contor2(img):
    copy = img.copy()
    copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
    copy = cv2.GaussianBlur(copy, (7, 7), 0)
    _, valor = cv2.threshold(copy, 40, 70, cv2.THRESH_BINARY )
    kernel = np.ones((5, 3), np.uint8)
    figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
    bordes = cv2.Canny(figura, 3, 3)
    contornos, _ = cv2.findContours(bordes, 
                                cv2.RETR_EXTERNAL, 
                                cv2.CHAIN_APPROX_SIMPLE)
    return contornos, figura

def contor(img):
    copy = img.copy()
    copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
    copy = cv2.GaussianBlur(copy, (7, 7), 0)
    _, valor = cv2.threshold(copy, 150, 220, cv2.THRESH_BINARY )
    kernel = np.ones((5, 3), np.uint8)
    figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
    bordes = cv2.Canny(figura, 3, 3)
    contornos, _ = cv2.findContours(bordes, 
                                cv2.RETR_EXTERNAL, 
                                cv2.CHAIN_APPROX_SIMPLE)
    return contornos, figura


count = 1
countFile = 0
#importar video
video = cv2.VideoCapture('video_objetos.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
print(f"Frames por segundo: {fps}")
if fps == 0:
    fps = 30
time = int(500 / fps)
cv2.namedWindow('Frame Original', cv2.WINDOW_NORMAL)
while True:
    nombre = ""
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow('Frame Original', frame) 
    key = cv2.waitKey(time) & 0xFF
    if key == ord('q'):
        break
    if key == ord(str(count)):
        nombre = f"Imagen_0{count}.jpg"
        cv2.imwrite(nombre, frame)
    if nombre == f"Imagen_0{count}.jpg":
        count+=1
for i in range(1, 6):
    if cv2.imread(f"Imagen_0{i}.jpg") is not None:
        countFile += 1
    else:
        print("ARCHIVO NO ENCOTRADO")
        break

if countFile == 5:
    img1 = cv2.imread("Imagen_01.jpg")
    cortono_img1, f1 = contor2(img1)
    img2 = cv2.imread("Imagen_02.jpg")
    cortono_img2, f2 = contor(img2)
    img3 = cv2.imread("Imagen_03.jpg")
    cortono_img3, f3 = contor(img3)
    img4 = cv2.imread("Imagen_04.jpg")
    cortono_img4, f4 = contor(img4)
    img5 = cv2.imread("Imagen_05.jpg")
    cortono_img5, f5 = contor(img5)

    imagenes = [img1, img2, img3, img4, img5]
    figuras = [f1, f2, f3, f4, f5]
    contornos = [cortono_img1, cortono_img2, cortono_img3, cortono_img4, cortono_img5]

    for i in range(5):
        cv2.drawContours(imagenes[i], 
                 contornos[i], 
                 -1, 
                 (0, 255, 0), 
                 2)
        lista = []
        for j in range(len(contornos[i])):
            area = cv2.contourArea(contornos[i][j])
            if area > 1000:
                lista.append(area)
                M = cv2.moments(contornos[i][j])
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    cv2.circle(imagenes[i], (cX, cY), 5, (255, 0, 0), -1)
                    print(f"Centro del contorno {i}: ({cX}, {cY})")
                    cv2.putText(imagenes[i], f"({cX}, {cY})", (cX - 20, cY - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

        cv2.putText(imagenes[i], f"Los objetos encontrados son: {len(lista)}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    for i in range(5):
        cv2.imshow(f"Imagen {i+1}", imagenes[i])
else:
    print("FALTA CAPTURAR IMAGENES")
    
    
video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
