import speech_recognition as sr
import pyttsx3
import pyjokes
import openai
import pywhatkit
import datetime
import pyautogui
import cv2
import easygui
import os

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
            audio = sr.Recognizer().listen(source, phrase_time_limit=5)
            try:
                print("RECONOCIENDO...")
                comando = sr.Recognizer().recognize_google(audio, language='es-MX')
                print(f"COMANDO {comando}")
                return comando.lower()
            except sr.UnknownValueError:
                hablarIA("No te he entendido, intenta otra vez.")
                continue

            except sr.RequestError as e:
                print(f"Error con el servicio: {e}")
                return ""

while True:
    comando = escucharIA()
    if "jarvis" in comando:
        hablarIA("¿En qué puedo ayudarte?")
        while True:
            comanedo = None
            comando = escucharIA()
            if "chiste" in comando:
                chiste = pyjokes.get_joke(language='es', category='all')
                hablarIA(chiste)
                break
    break