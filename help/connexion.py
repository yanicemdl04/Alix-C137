from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from subprocess import call
import sqlite3

window = Tk()
window.title("Formulaire")
window.geometry("1150x720")
window.minsize(480, 360)
window.iconbitmap("ia2.ico")
window.config(background='#26A0B6')

CHOIX = ["homme", 'femme']


#titre 
window.columnconfigure(3, weight=2)
Label_title = Label(window, text="CONNEXION", font=("times new roman", 20, "bold"),bg='#26A0B6', fg='WHITE')
Label_title.grid(row=0, column=2, columnspan=4, padx=40, pady=40, sticky="we")

# Création du widget Canvas
canvas = Canvas(window, width=350, height=180, bg='#26A0B6', highlightthickness=0)
canvas.grid(row=1, column=2, columnspan=2)
# Chargement des images
image2 = PhotoImage(file="team2.png")
# Placement des images sur le canvas
canvas.create_image(280, 100 ,image=image2)


#databasa
def submit():
    conn = sqlite3.connect('bdd.sqlite')
    c = conn.cursor()

    valeurs = {'nom_client': e_nom_clients.get(),
                'prenom_client': e_prenom_clients.get(),
                'adresse': e_adresse.get(),
                'telephone': e_tel.get()}

    c.execute("INSERT INTO clients (nom_client, prenom_client, adresse, telephone) VALUES (:nom_client, :prenom_client, :adresse, :telephone)", valeurs)
    conn.commit()
    conn.close()
    
    e_nom_clients.delete(0, END)
    e_prenom_clients.delete(0, END)
    e_adresse.delete(0, END)
    e_tel.delete(0, END)


def chambre() :
    window.destroy()
    call(['python', 'chambre.py'])


champs = {
    'jour': tk.StringVar(),
    'choix': tk.IntVar()
}

#informations du formulaire
nom_clients = Label(window, text="nom_clients : ")
prenom_clients = Label(window, text="prenom_clients : ")
adresse = Label(window, text="adresse : ")
tel = Label(window, text="telephone : ")

e_nom_clients = Entry(window, width=60)
e_prenom_clients = Entry(window, width=60)
e_adresse = Entry(window, width=60)
e_tel = Entry(window, width=60)


nom_clients.grid(row=2, column=2, padx=55, sticky="e")
e_nom_clients.grid(row=2, column=3, padx=5, pady=10)

prenom_clients.grid(row=3, column=2, padx=55, pady=10, sticky="e")
e_prenom_clients.grid(row=3, column=3, padx=5, pady=10)

adresse.grid(row=4, column=2, padx=55, pady=10, sticky="e")
e_adresse.grid(row=4, column=3, padx=5, pady=10)

for i,rb_label in enumerate(CHOIX):
    label = Label(window, text="Genre : ")
    label.grid(row=8, column=2, padx=55, pady=10, sticky="e")
    rb = ttk.Radiobutton(window, text=rb_label, value=i, variable=champs['choix'])
    rb.grid(column=2+i, row=8, pady=10, columnspan=len(CHOIX))

nxt = Button(window, text="Suivant", width=35, command=lambda: (submit(), chambre()))
nxt.grid(row=9, column=3, columnspan=2)


#afficher
window.mainloop()
