import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime
from tkinter import *
import tkinter as tk
from subprocess import call

listerner = sr.Recognizer() # variable permettant d'écouter
engine = ttx.init() # initialisation
voices = engine.getProperty('voices') # voix
engine.setProperty('voice', 'french') # choisir la langue de sortie

def parle(text):
    engine.say(text) # ce qu'on dira qu'il va récupérer
    engine.runAndWait() # écouter nos paroles

def ecoute():
    try:
        with sr.Microphone() as source: # tant que micro est ouvert
            print("parle")
            voix = listerner.listen(source)
            command = listerner.recognize_google(voix, language='fr-FR')
            return command
    except sr.UnknownValueError: # si la connexion est mauvaise
        print("Google Speech Recognition n'a pas pu comprendre l'audio")
    except sr.RequestError as e: # si la requête à Google a échoué
        print(f"La requête à Google Speech Recognition a échoué; {e}")

def assistante():
    command = ecoute()
    print(command)
    if 'boujour' in command: # si le message contient bonjour exécute l'action
        parle('bonjour frero tranquille ou quoi?')
    elif 'oui ça va tranquille et toi' in command:
        parle('oh tu sais ça va de mon côté, du coup tu as besoin de quoi?')
    elif 'met la chanson de ' in command:
        chanteur = command.replace('met la chanson de ', '')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    elif 'il est quelle heure' in command:
        heure = datetime.datetime.now().strftime('%H:%M')
        print('il est : ' + heure)
        parle(heure)
    elif 'quel est ton nom' in command:
        parle('Je réponds au nom de Alix C137')

root = Tk()
root.title("AI QUESTION")
root.attributes('-fullscreen', True)
root.minsize(480, 360)
root.iconbitmap("ia2.ico")
root.config(background='WHITE')

fondec = Canvas(root, width=1500, height=460, bg="#100628", highlightthickness=0)
fondec.place(x=0, y=0)
image = PhotoImage(file="robot.png")
fondec.create_image(670, 200, image=image) # le premier de g à d, le deuxieme de h en b

button = Button(root, text="Fermer", bg='WHITE', command=root.quit)
button.place(x=1200, y=0, width=50)

vocale = Canvas(root, width=520, height=250, bg='WHITE', highlightthickness=0)
vocale.place(x=670, y=480)
image3 = PhotoImage(file="vocaliste2.png")
vocale.create_image(200, 130, image=image3)

button = Button(root, text="PARLER", bg='#100628', command=assistante)
button.place(x=300, y=600, width=100)

root.mainloop()
