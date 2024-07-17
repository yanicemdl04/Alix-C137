import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit  # module permettant de recuperer des trucs sur l'internet
import datetime

listener = sr.Recognizer()  # variable permettant d'ecouter
engine = ttx.init()  # initialisation

voices = engine.getProperty('voices')  # voix
engine.setProperty('voice', 'french') # choisir la langue de sortie


# fonction permettant de parler
def parle(text):
    engine.say(text)  # ce qu'on dira qu'il va recuper
    engine.runAndWait()  # ecouter nos paroles
    

def ecoute():
    try:
        with sr.Microphone() as source:  # tant que le micro est ouvert
            print("parle")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')

    except sr.UnknownValueError:  # Si la parole n'est pas clairement entendue
        parle("Je n'ai pas compris, pouvez-vous répéter?")
    except sr.RequestError:  # Si une erreur se produit lors de la requête de reconnaissance
        parle("Désolé, je ne peux pas accéder aux services de reconnaissance vocale.")
    return command

def assistante():
    command = ecoute()
    print(command)
    if 'bonjour' in command:  # si le message contient bonjour, exécute l'action
        parle('bonjour tranquille ou quoi?')
    elif 'oui ça va tranquille et toi' in command:
        parle('oh tu sais ça va de mon coté, du coup tu as besoin de quoi?')
    elif 'est-ce que je suis beau' in command:
        parle('mdrrrr tu vaux mieux que ça')
    elif "suis-je bien habillé aujourd'hui" in command:
        parle('oui comme dab')
    elif "tu es méchante" in command:
        parle('oh tu abuses passe à autre chose')
    elif 'quel est ton nom' in command:
        parle('Je repond au nom de Alix C137')

    elif 'met la chanson de ' in command:
        chanteur = command.replace('met la chanson de ', '')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    elif 'quel temps il fera demain' in command:
        pywhatkit.search("Quel temps fera-t-il demain")
    elif 'quelle est la capitale de ' in command:
        capitale = command.replace('quelle est la capitale de', '')
        print(capitale)
    elif 'il est quelle heure' in command:
        heure = datetime.datetime.now().strftime('%H:%M')
        parle('il est : ' + heure)
    else:
        parle("Désolé, je ne comprends pas cette commande.")

