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

def validate_entries():
    # Vérifier si tous les champs sont remplis
    if not e_adresse.get() or not mdp.get():
        messagebox.showinfo("", "Veuillez remplir tous les champs")
        return False
    return True

def submit():
    if not validate_entries():
        return
    
    email = e_adresse.get()
    password = mdp.get()
    
    conn = sqlite3.connect('database/alix.sqlite')
    c = conn.cursor()
    
    c.execute("SELECT * FROM acces WHERE email = ? AND mdp = ?", (email, password))
    result = c.fetchone()
    conn.close()
    
    if result:
        run_script()
    else:
        messagebox.showerror("Erreur", "Email ou mot de passe incorrect")

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
image2 = PhotoImage(file="images/fermer2.png")
# Placement des images sur le canvas
user.create_image(70, 70, image=image2)

button = Button(root, text="Fermer", bg='WHITE', command=root.quit)
button.place(x=1200, y=0, width=50)

# Les differents champs
adresse = Label(root, text="Email : ")
adresse.place(x=680, y=280)
e_adresse = Entry(root, width=45)
e_adresse.place(x=780, y=280)

# Création d'un widget Label pour indiquer le champ de saisie du mot de passe
e_mdp_label = Label(root, text="Mot de passe : ")
e_mdp_label.place(x=680, y=340)
# Création d'un widget Entry pour saisir le mot de passe
mdp = Entry(root, width=45, show='*')
mdp.place(x=780, y=340)

button = Button(root, text="Connexion", command=submit)
button.place(x=820, y=400, width=150)

# Lancer la boucle principale de la fenêtre
root.mainloop()