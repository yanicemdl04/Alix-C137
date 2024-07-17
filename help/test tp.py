import tkinter as tk
import speech_recognition as sr
import time

class OndulationApp:
    def __init__(self, window):
        self.window = window
        self.canvas = tk.Canvas(window, width=500, height=200, bg='white')
        self.canvas.pack()
        self.recognizer = sr.Recognizer()
        self.listen_to_speech()

    def listen_to_speech(self):
        with sr.Microphone() as source:
            print("Parlez maintenant...")
            audio = self.recognizer.listen(source)
            try:
                recognized_text = self.recognizer.recognize_google(audio).lower()
                print(f"Mots reconnus: {recognized_text}")
                self.animate_wave(recognized_text.split())
            except Exception as e:
                print(e)
                self.listen_to_speech()

    def animate_wave(self, words):
        for word in words:
            self.draw_wave(word)
            self.window.after(1000, self.clear_wave)  # Attendre 1 seconde avant de commencer la prochaine onde

    def draw_wave(self, word):
        x = 10
        for letter in word:
            self.canvas.create_line(x, 100, x+20, 200, fill='blue', width=5)
            x += 30
        self.window.update()

    def clear_wave(self):
        self.canvas.delete('all')  # Effacer l'écran avant de redessiner la prochaine onde

if __name__ == "__main__":
    window = tk.Tk()
    app = OndulationApp(window)
    window.mainloop()
