from flask import Flask, redirect
app = Flask(__name__)

@app.route('/interface1')
def interface1():
    # Code pour ouvrir l'interface Tkinter 1
    return redirect("main.py")  # Remplacez ceci par le chemin réel vers votre script Tkinter

@app.route('/interface2')
def interface2():
    # Code pour ouvrir l'interface Tkinter 2
    return redirect("program.py")  # Remplacez ceci par le chemin réel vers votre script Tkinter

if __name__ == '__main__':
    app.run(debug=True)
