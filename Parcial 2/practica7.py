import pyttsx3

voz = pyttsx3.init()
voces = voz.getProperty('voices')
voz.setProperty('voice', voces[0].id)
voz.setProperty('rate', 150)
voz.setProperty('volume', 1.0)
 #cancion corazon encantado de dragon ball z
voz.say("Tu sonrisa tan resplandeciente, " \
"A mi corazón deja encantado, " \
"Ven toma mi mano " \
"Para huir de esta terrible oscuridad ")
voz.runAndWait()