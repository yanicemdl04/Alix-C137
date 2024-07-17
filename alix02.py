# Importation des bibliothèques nécessaires
import tkinter as tk
import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime

# Définition de la classe principale de l'application
class AssistantApp:
    def __init__(self, root):  # Initialisation de l'objet
        self.root = root  # Stockage de la fenêtre principale
        self.root.title("Assistant Vocal")  # Nom de la fenêtre
        self.create_widgets()  # Création des widgets
        
        # Initialisation de l'objet de reconnaissance vocale
        self.listener = sr.Recognizer()
        # Initialisation de l'engine de synthèse vocale
        self.engine = ttx.init()
        
        # Sélection de la voix française
        self.voices = self.engine.getProperty('voices')
        for voice in self.voices:
            if "french" in voice.languages[0]:  # Si la langue de la voix est française
                self.engine.setProperty('voice', voice.id)  # Utiliser cette voix
                break

    def create_widgets(self):  # Méthode pour créer les widgets (éléments graphiques)
        self.text_area = tk.Text(self.root, height=10, width=50)  # Zone de texte pour afficher les interactions
        self.text_area.pack()  # Empiler la zone de texte dans la fenêtre
        
        self.listen_button = tk.Button(self.root, text="Écouter", command=self.assistante)  # Bouton pour démarrer l'écoute
        self.listen_button.pack()  # Empiler le bouton dans la fenêtre

    def parle(self, text):  # Méthode pour faire parler l'assistant
        self.engine.say(text)  # Commande pour dire le texte
        self.engine.runAndWait()  # Attendre que la phrase soit complètement prononcée
        self.text_area.insert(tk.END, f"Assistant: {text}\n")  # Ajouter le texte parlé à la zone de texte

    def ecoute(self):  # Méthode pour écouter les commandes utilisateur
        command = ""  # Variable pour stocker la commande reçue
        try:
            with sr.Microphone() as source:  # Utiliser le microphone en tant que source sonore
                self.text_area.insert(tk.END, "Parlez maintenant...\n")  # Indication à l'utilisateur de commencer à parler
                voix = self.listener.listen(source)  # Écouter la voix
                command = self.listener.recognize_google(voix, language='fr-FR')  # Reconnaissance de la parole
                self.text_area.insert(tk.END, f"Vous: {command}\n")  # Afficher la commande reçue
        except sr.UnknownValueError:  # Si la parole n'est pas clairement entendue
            self.parle("Je n'ai pas compris, pouvez-vous répéter?")
        except sr.RequestError:  # Si une erreur se produit lors de la requête de reconnaissance
            self.parle("Désolé, je ne peux pas accéder aux services de reconnaissance vocale.")
        return command  # Retourner la commande reçue

    def assistante(self):  # Méthode principale pour gérer les commandes
        command = self.ecoute()  # Obtenir la commande de l'utilisateur
        if 'bonjour' in command:
            self.parle('Bonjour, tranquille ou quoi?')
        elif 'oui ça va tranquille et toi' in command:
            self.parle('Oh tu sais ça va de mon côté, du coup tu as besoin de quoi?')
        elif 'est-ce que je suis beau' in command:
            self.parle('Mdrrrrr tu vaux mieux que ça.')
        elif "suis-je bien habillé aujourd'hui" in command:
            self.parle('Oui, comme d’hab.')
        elif "ah tu es méchante" in command:
            self.parle('Oh tu abuses, passe à autre chose.')
        elif 'quel est ton nom' in command:
            self.parle('Je réponds au nom de Alix C137.')
        elif 'met la chanson de ' in command:
            chanteur = command.replace('met la chanson de ', '')  # Extraire le nom du chanteur
            self.parle(f"Je mets la chanson de {chanteur}")
            pywhatkit.playonyt(chanteur)  # Jouer la chanson sur YouTube
        elif 'quel temps il fera demain' in command:
            pywhatkit.search("Quel temps fera-t-il demain")  # Recherche météo
            self.parle("Voici les prévisions pour demain.")
        elif 'quelle est la capitale de ' in command:
            capitale = command.replace('quelle est la capitale de ', '')  # Extraire le pays
            self.parle(f"La capitale de {capitale} est ...")
            pywhatkit.search(f"Quelle est la capitale de {capitale}")  # Recherche de la capitale
        elif 'il est quelle heure' in command:
            heure = datetime.datetime.now().strftime('%H:%M')  # Obtenir l'heure actuelle
            self.parle(f'Il est : {heure}')
        else:
            self.parle("Désolé, je ne comprends pas cette commande.")

# Exécution de l'application si elle est exécutée en tant que script principal
if __name__ == "__main__":
    root = tk.Tk()  # Création de la fenêtre principale
    app = AssistantApp(root)  # Création de l'instance de l'application
    root.mainloop()  # Lancement de la boucle principale de l'interface graphique
