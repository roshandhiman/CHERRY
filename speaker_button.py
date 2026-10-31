import subprocess
import threading
import tkinter as tk
speaker_on=True
def speak(text):
    if not speaker_on or not text.strip():
        return
    def run():
        subprocess.run(["say","-v","Samantha",text],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    threading.Thread(target=run,daemon=True).start()
def toggle_speaker(btn):
    global speaker_on
    speaker_on=not speaker_on
    btn.config(text="🔊" if speaker_on else "🔇")
def create_speaker_button(parent):
    btn=tk.Button(parent,text="🔊",font=("Arial",14),bg="black",fg="white",bd=0,highlightthickness=0)
    btn.config(command=lambda:toggle_speaker(btn))
    return btn

