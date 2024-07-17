from tkinter import *
import importlib.util
from tkinter import messagebox 
import sqlite3

root = Tk()
root.title("Alix C137")
root.attributes('-fullscreen', True)
root.minsize(480, 360)
root.iconbitmap("images/ai.ico")
root.config(background='#F7F7F7')


def run_script():
    root.destroy()
    # Le chemin complet vers le script que vous voulez exécuter
    script_path = r"J:\2. Development test\Test for python\projet fda\(4)program.py"
    
    # Importer et exécuter le script
    spec = importlib.util.spec_from_file_location("questions_module", script_path)
    questions_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(questions_module)

# Création du widget image bleu
canvas = Canvas(root, width=575, height=780, bg='#26A0B6', highlightthickness=0)
canvas.place(x=0, y=0)
# Chargement des images
image = PhotoImage(file="images/ai3-removebg-preview.png")
# Placement des images sur le canvas
canvas.create_image(287, 360, image=image)

# Création du widget image fermer
user = Canvas(root, width=250, height=250, bg="#F7F7F7", highlightthickness=0)
user.place(x=820, y=110)
# Chargement des images
image2 = PhotoImage(file="images/user1.png")
# Placement des images sur le canvas
user.create_image(70, 70, image=image2)

button = Button(root, text="Fermer", bg='WHITE', command=root.quit)
button.place(x=1200, y=0, width=50)

# Les differents champs
Label(root, text="Email : ").place(x=680, y=280)
e_adresse = Entry(root, width=45)
e_adresse.place(x=780, y=280)

Label(root, text="Nom : ").place(x=680, y=310)
e_nom = Entry(root, width=45)
e_nom.place(x=780, y=310)

Label(root, text="Prenom : ").place(x=680, y=340)
e_prenom = Entry(root, width=45)
e_prenom.place(x=780, y=340)


def masquer_mot_de_passe(event):
    mot_entre = mdp.get()
    mot_masque = mot_entre[0] + "*" * (len(mot_entre) - 2) + mot_entre[-1]
    mdp.delete(0, 'end')
    mdp.insert(0, mot_masque)

# Création d'un widget Label pour indiquer le champ de saisie du mot de passe
e_mdp_label = Label(root, text="Mot de passe : ")
e_mdp_label.place(x=680, y=370)
# Création d'un widget Entry pour saisir le mot de passe
mdp = Entry(root, width=45, show='*')
mdp.place(x=780, y=370)
# Fonction pour masquer le mot de passe lorsqu'une touche est appuyée
mdp.bind("<KeyRelease>", masquer_mot_de_passe)

def validate_entries():
    # Vérifier si tous les champs sont remplis
    if not e_adresse.get() or not e_nom.get() or not e_prenom.get() or not mdp.get():
        messagebox.showinfo("", "Veuillez remplir tous les champs")
        return False
    return True

def user_exists(email):
    conn = sqlite3.connect('database/alix.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM creer WHERE email = ?", (email,))
    result = c.fetchone()
    conn.close()
    return result is not None

def submit():
    if not validate_entries():
        return
    
    email = e_adresse.get()
    if user_exists(email):
        messagebox.showinfo("", "L'utilisateur existe déjà")
        return

    conn = sqlite3.connect('database/alix.sqlite')
    c = conn.cursor()
    
    valeurs = {'email': email, 'mdp': mdp.get(), 'nom': e_nom.get(), 'prenom': e_prenom.get()}
    c.execute("INSERT INTO creer (email, mdp, nom, prenom) VALUES (:email, :mdp, :nom, :prenom)", valeurs)
    conn.commit()
    conn.close()
    
    mdp.delete(0, END)
    e_adresse.delete(0, END)
    e_nom.delete(0, END)
    e_prenom.delete(0, END)

button1 = Button(root, text="Enregistrer", command=submit)
button1.place(x=820, y=420, width=150)

button2 = Button(root, text="Connexion", command=run_script)
button2.place(x=820, y=470, width=150)

# Lancer la boucle principale de la fenêtre
root.mainloop()