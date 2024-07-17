from tkinter import *
import tkinter as tk
import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit  # module permettant de récupérer des trucs sur l'internet
import datetime

# Initialisation du module d'écoute et de synthèse vocale
listener = sr.Recognizer()
engine = ttx.init()

voices = engine.getProperty('voices')  # voix
engine.setProperty('voice', 'french')  # choisir la langue de sortie

# Fonction permettant de parler
def parle(text):
    engine.say(text)
    engine.runAndWait()

# Fonction permettant d'écouter la commande de l'utilisateur
def ecoute():
    try:
        with sr.Microphone() as source:
            print("Parle")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')
    except sr.UnknownValueError:
        parle("Je n'ai pas compris, pouvez-vous répéter?")
        return ""
    except sr.RequestError:
        parle("Désolé, je ne peux pas accéder aux services de reconnaissance vocale.")
        return ""
    return command

# Fonction principale de l'assistant
def assistante():
    command = ecoute()
    print(command)
    if 'bonjour' in command:
        parle('bonjour tranquille ou quoi?')
    elif 'oui ça va tranquille et toi' in command:
        parle('oh tu sais ça va de mon côté, du coup tu as besoin de quoi?')
    elif 'est-ce que je suis beau' in command:
        parle('mdrrrr tu vaux mieux que ça')
    elif "suis-je bien habillé aujourd'hui" in command:
        parle('oui comme dab')
    elif "tu es méchante" in command:
        parle('oh tu abuses passe à autre chose')
    elif 'quel est ton nom' in command:
        parle('Je réponds au nom de Alix C137')
    elif 'met la chanson de ' in command:
        chanteur = command.replace('met la chanson de ', '')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    elif 'quel temps il fera demain' in command:
        pywhatkit.search("Quel temps fera-t-il demain")
    elif 'quelle est la capitale de ' in command:
        capitale = command.replace('quelle est la capitale de ', '')
        print(capitale)
    elif 'il est quelle heure' in command:
        heure = datetime.datetime.now().strftime('%H:%M')
        parle('il est : ' + heure)
    else:
        parle("Désolé, je ne comprends pas cette commande.")

# Fonction pour mettre à jour la zone de texte dans l'interface graphique
def update_text_area(response):
    text_area.insert(tk.END, f"Alix: {response}\n")
    print(text_area)

# Fonction appelée lorsque l'utilisateur clique sur le bouton PARLER
def on_speak():
    response = assistante()
    update_text_area(response)

# Configuration de l'interface graphique Tkinter
root = Tk()
root.title("AI QUESTION")
root.attributes('-fullscreen', True)
root.minsize(480, 360)
root.iconbitmap("images/ia2.ico")
root.config(background='WHITE')

# Création du canevas de fond
fondec = Canvas(root, width=1500, height=460, bg="#100628", highlightthickness=0)
fondec.place(x=0, y=0)
image = PhotoImage(file="images/robot.png")
fondec.create_image(670, 200, image=image)

# Bouton pour fermer l'application
button_close = Button(root, text="Fermer", bg='WHITE', command=root.quit)
button_close.place(x=1200, y=0, width=50)

# Bouton pour déclencher la commande de parole
button_speak = Button(root, text="PARLER", bg='#100628', fg="white", command=on_speak)
button_speak.place(x=300, y=600, width=100, height=40)

# Ajout d'une zone de texte pour afficher les interactions
text_area = Text(root, wrap=WORD, bg='lightgrey')
text_area.place(x=900, y=500, width=400, height=200)

root.mainloop()