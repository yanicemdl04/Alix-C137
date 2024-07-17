from tkinter import Tk, Label, Entry, Button, Canvas, PhotoImage, StringVar
from subprocess import call
from tkinter import messagebox 
import sqlite3

root = Tk()
root.title("Alix C137")
root.attributes('-fullscreen', True)
root.minsize(480, 360)
root.iconbitmap("images/ai.ico")
root.config(background='#F7F7F7')

def Portail():
    root.destroy()
    call(['python', 'program.py'])



def validate_entries():
    # Vérifier si tous les champs sont remplis
    if not e_mdp_label.get() or not e_adresse.get():
        messagebox.showinfo("", "Veuillez remplir tous les champs") 
        return False
    else:
        return True



# Création du widget Canvas
user_canvas = Canvas(root, width=250, height=250, bg="#F7F7F7", highlightthickness=0)
user_canvas.place(x=820, y=110)
# Chargement des images
user_image = PhotoImage(file="images/user1.png")
# Placement des images sur le canvas
user_canvas.create_image(70, 70,image=user_image)

close_button = Button(root, text="Fermer", bg='WHITE', command=root.quit)
close_button.place(x=1200, y=0, width=50)

# Création du widget Canvas principal
main_canvas = Canvas(root, width=575, height=780, bg='#26A0B6', highlightthickness=0)
main_canvas.place(x=0, y=0)
# Chargement des images
main_image = PhotoImage(file="images/ai3-removebg-preview.png")
# Placement des images sur le canvas
main_canvas.create_image(287, 360,image=main_image)

# Les différents champs
email_label = Label(root, text="Email : ")
email_label.place(x=680, y=280)
email_entry = Entry(root, width=45)
email_entry.place(x=780, y=280)

password_label = Label(root, text="Mot de passe : ")
password_label.place(x=680, y=340)
password_entry = Entry(root, width=45, show='*')
password_entry.place(x=780, y=340)

def submit():
    conn = sqlite3.connect('database/alix.sqlite')
    c = conn.cursor()

    values = {'email': email_entry.get(),
              'password': password_entry.get()
              }

    c.execute("INSERT INTO acces (email, password) VALUES (:email, :password)", values)
    conn.commit()
    conn.close()
    
    password_entry.delete(0, 'end')
    email_entry.delete(0, 'end')

def mask_password(event):
    entered_password = password_entry.get()
    masked_password = entered_password[0] + "*" * (len(entered_password) - 2) + entered_password[-1]
    password_entry.delete(0, 'end')
    password_entry.insert(0, masked_password)

password_entry.bind("<KeyRelease>", mask_password)

register_button = Button(root, text="Enregistrer", command=submit)
register_button.place(x=820, y=400, width=150)

login_button = Button(root, text="Connexion", command=lambda: (Portail()))
login_button.place(x=820, y=450, width=150)

# Lancer la boucle principale de la fenêtre
root.mainloop()
