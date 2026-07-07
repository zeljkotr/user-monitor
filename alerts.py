import tkinter as tk
from tkinter import messagebox
import threading
from datetime import datetime

vec_prikazano = set()

def popup(naslov, poruka):
    def prikazi():
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        root.lift()
        root.focus_force()
        messagebox.showwarning(naslov, poruka)
        root.destroy()
    
    t = threading.Thread(target=prikazi)
    t.daemon = True
    t.start()

def upozori(tip, poruka):
    if tip not in vec_prikazano:
        vec_prikazano.add(tip)
        vreme = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{vreme} | ALERT: {poruka}")
        popup("⚠️ UPOZORENJE", poruka)

def ocisti(tip):
    vec_prikazano.discard(tip)