import speech_recognition as sr
import sys
import pyttsx3
import threading

def hablar(texto):
    voz = pyttsx3.init()
    voces = voz.getProperty('voices')
    voz.setProperty('voice', voces[0].id)
    voz.setProperty('rate', 150)
    voz.setProperty('volume', 1.0)
    voz.say(texto)
    voz.runAndWait()

escuchar = sr.Recognizer()

while True:
    with sr.Microphone() as recurso:
        print("ESCUCHANDO....")
        audio = escuchar.listen(recurso, phrase_time_limit=5)
        try:
            print("RECONOCIENDO...")
            text = escuchar.recognize_google(audio, language='es-US')
            print(text)
            hilo = threading.Thread(target=hablar(text))
            hilo.start()
            hilo.join()
            if text in "salir":
                break
            if text == "salir":
                break
        except Exception as e:
            print("No entendi vuelve a intentarlo")
            print(e)