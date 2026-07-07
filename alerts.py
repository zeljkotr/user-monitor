import tkinter as tk
from tkinter import messagebox
import threading
import time
from datetime import datetime

vec_prikazano = set()

def splash():
    def prikazi():
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        root.lift()
        root.focus_force()
        messagebox.showinfo(
            "User Monitor",
            "User Monitor v1.0\n\n"
            "Monitoring je aktivan!\n\n"
            "Pratim: CPU, RAM, Mrezu\n"
            "Chrome i iVMS-4200\n\n"
            "Autor: Zeljko Tripcevski\n"
            "IT Team Lead @ MTC Nissal"
        )
        root.destroy()

    t = threading.Thread(target=prikazi)
    t.daemon = True
    t.start()
    time.sleep(2)

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