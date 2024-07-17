from tkinter import *
from subprocess import call

root = Tk()
root.title("Alix C137")
root.attributes('-fullscreen', True)
root.minsize(480, 360)
root.iconbitmap("images/ai.ico")
root.config(background='white')



def Utilisateur() :
    root.destroy()
    call(['python', '(2)utilisateur.py'])


def Nouveau() :
    root.destroy()
    call(['python', '(3)creer.py'])



#bouton quitter
button3 = Button(root, text="Fermer", bg='WHITE', command=root.quit)
button3.place(x=1200, y=0, width=50)


# Création du widget pour le bouton connexion
canvas = Canvas(root, width=700, height=780, bg="#26A0B6", highlightthickness=0)
canvas.place(x=0, y=0)
# Chargement des images
image = PhotoImage(file="images/fermer2.png")
canvas.create_image(480, 400 ,image=image)

button = Button(root, text="Connexion", width=120, command=lambda: (Utilisateur()))
button.place(x=400, y=500, width=150)



# Création du widget pour le bouton creation
user = Canvas(root, width=200, height=200, bg="white", highlightthickness=0)
user.place(x=820, y=300)
# Chargement des images
image2 = PhotoImage(file="images/user1.png")
user.create_image(70, 100 ,image=image2)

button1 = Button(root, text="Créer un compte", width=120, command=lambda: (Nouveau()))
button1.place(x=820, y=500, width=150)



# Lancer la boucle principale de la fenêtre
root.mainloop()
