import speech_recognition as sr
import pyttsx3
# import pyjokes
import pywhatkit
import datetime
import pyautogui
import cv2
import easygui
import os
import json
import subprocess
import random

busquedas = ['buscar en google', 'abrir google', 'google']

def guardar_imagen(imagen):
    ruta = easygui.diropenbox(title="Selecciona la carpeta para guardar la imagen")
    if ruta:
        nombre_archivo = "captura_pantalla.jpg"
        ruta_completa = os.path.join(ruta, nombre_archivo)
        cv2.imwrite(ruta_completa, imagen)
        print(f"Imagen guardada en: {ruta_completa}")
    else:
        print("No se seleccionó ninguna carpeta. La imagen no se guardará.")
    
    

escuchar = sr.Recognizer()
def hablarIA(mensaje):
    hablar = pyttsx3.init()
    voces = hablar.getProperty('voices')
    hablar.setProperty('voice', voces[3].id)
    velocidad = hablar.getProperty('rate')
    hablar.setProperty('rate', velocidad - 20)
    hablar.say(mensaje)
    hablar.runAndWait()

def escucharIA():
    while True:
        with sr.Microphone() as source:
            print("ESCUCHANDO...")
            audio = escuchar.listen(source, phrase_time_limit=5)
            try:
                print("RECONOCIENDO...")
                comando = escuchar.recognize_google(audio, language='es-MX')
                print(f"COMANDO {comando}")
                return comando.lower()
            except sr.UnknownValueError:
                hablarIA("No te he entendido, intenta otra vez.")
                continue

            except sr.RequestError as e:
                print(f"Error con el servicio: {e}")
                return ""

# def decirChiste():
#     chiste = pyjokes.get_joke(language='es', category='all')
#     hablarIA(chiste)

def bienvenida():
    hablarIA("Hola, soy tu asistente virtual joven Francisco. ¿En qué puedo ayudarte hoy?")

bienvenida()
while True:
    comando = escucharIA()
    hablarIA(f"Has dicho: {comando}")
    if "chiste" in comando:
        # hablarIA("Claro, aquí tienes un chiste muy bueno francisco.")
        # decirChiste()
        with open("comandos.json", "r", encoding="utf-8") as file:
            datos = json.load(file)
        list_chistes = datos["chiste"]
        chiste_aletorio = random.choice(list_chistes)
        hablarIA(f"Claro, aquí tienes un chiste muy bueno francisco. {chiste_aletorio}")
        
    elif 'maneskin' in comando:
        hablarIA("reproduciendo Maneskin en YouTube, joven Francisco.")
        pywhatkit.playonyt("YouTube maneskin")    
        quit()
    elif any(busqueda in comando for busqueda in busquedas):
        buscar = comando.replace("buscar en google", "").replace("abrir google", "").replace("google", "").strip()
        if buscar:
            hablarIA(f"Buscando {buscar} en Google, joven Francisco.")
            pywhatkit.search(buscar)
        else:
            hablarIA("No se ha especificado qué buscar, joven Francisco.")
    elif "mane" in comando:
        hablarIA("insultar a Emanuel, joven Francisco.")
        pywhatkit.sendwhatmsg_instantly("+523319258337", "Emanuel es un idiota")
    elif "hora" in comando:
        hora_actual = datetime.datetime.now().strftime("%H:%M")
        hablarIA(f"La hora actual es {hora_actual}, joven Francisco.")
    elif "fecha" in comando:
        fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
        hablarIA(f"La fecha actual es {fecha_actual}, joven Francisco.")

    elif "capturar pantalla" in comando:
        hablarIA("Capturando pantalla, joven Francisco.")
        screenshot = pyautogui.screenshot()
        dato = "C://Users/Eduar/OneDrive/Documentos/screenshot.jpg"
        screenshot.save(dato)
        mostrar_imagen = cv2.imread(dato)
        guardar_imagen(mostrar_imagen)
        cv2.namedWindow("Captura de Pantalla", cv2.WINDOW_NORMAL)
        cv2.imshow("Captura de Pantalla", mostrar_imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif "abrir" in comando:
        with open("comandos.json", "r", encoding="utf-8") as file:
            datos = json.load(file)
        
        comando_abre = comando.replace("abrir", "").strip()
        if comando_abre in datos["abre"]:
            ruta_programa = datos["abre"][comando_abre]
            hablarIA(f"Abriendo {comando_abre}, joven Francisco.")
            subprocess.Popen(ruta_programa)
        else:
            hablarIA(f"No tengo un comando para abrir {comando_abre}, joven Francisco.")
    elif comando == "salir":
        hablarIA("Adiós, que tengas un buen día, joven Francisco.")
        break
    
