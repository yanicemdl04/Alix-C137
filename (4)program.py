from tkinter import *
import importlib.util


def run_script():
    root.destroy()
    # Le chemin complet vers le script que vous voulez exécuter
    script_path = r"J:\2. Development test\Test for python\projet fda\(5)questions.py"
    
    # Importer et exécuter le script
    spec = importlib.util.spec_from_file_location("questions_module", script_path)
    questions_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(questions_module)

root = Tk()
root.title("Alix C137")
root.attributes('-fullscreen', True)
root.minsize(480, 360)
root.iconbitmap("images/ai.ico")
root.config(background='#F7F7F7')

# Création du widget Canvas
canvas = Canvas(root, width=1500, height=800, bg='#0C2157', highlightthickness=0)
canvas.place(x=0, y=0)
# Chargement des images
image8 = PhotoImage(file="images/robot1.png")
# Placement des images sur le canvas
canvas.create_image(700, 370, image=image8)

button = Button(root, text="Fermer", bg='WHITE', command=root.quit)
button.place(x=1200, y=0, width=50)

button2 = Button(root, text="QUESTIONS", font=("arial", 18, "bold"), bg='#26A0B6', fg='WHITE', command=run_script)
button2.place(x=600, y=330, width=190, height=55)

# Lancer la boucle principale de la fenêtre
root.mainloop()