import tkinter as tk
from tkinter import messagebox
import config
import os
import sys

def otvori_settings():
    cfg = config.ucitaj()

    prozor = tk.Tk()
    prozor.title("User Monitor - Podesavanja")
    prozor.geometry("350x300")
    prozor.resizable(False, False)
    prozor.attributes("-topmost", True)
    prozor.configure(bg="#1a1a2e")

    fg = "#ffffff"
    bg = "#1a1a2e"
    entry_bg = "#16213e"

    tk.Label(prozor, text="⚙️ PODESAVANJA",
            fg="#00d4ff", bg=bg,
            font=("Consolas", 12, "bold")).grid(
            row=0, columnspan=2, pady=15)

    def label(tekst, row):
        tk.Label(prozor, text=tekst, fg=fg, bg=bg,
                font=("Consolas", 10)).grid(
                row=row, column=0, padx=20, pady=8, sticky="w")

    def entry(vrednost, row):
        var = tk.StringVar(value=str(vrednost))
        e = tk.Entry(prozor, textvariable=var,
                    bg=entry_bg, fg=fg,
                    font=("Consolas", 10), width=10,
                    insertbackground=fg)
        e.grid(row=row, column=1, padx=20, pady=8)
        return var

    label("CPU prag (%):", 1)
    cpu_var = entry(cfg["CPU_PRAG"], 1)

    label("RAM prag (%):", 2)
    ram_var = entry(cfg["RAM_PRAG"], 2)

    label("Mreza prag (MB/s):", 3)
    mreza_var = entry(cfg["MREZA_PRAG_MB"], 3)

    label("Interval provere (s):", 4)
    interval_var = entry(cfg["INTERVAL"], 4)

    def sacuvaj_i_restartuj():
        try:
            novi = {
                "CPU_PRAG": int(cpu_var.get()),
                "RAM_PRAG": int(ram_var.get()),
                "MREZA_PRAG_MB": int(mreza_var.get()),
                "INTERVAL": int(interval_var.get())
            }
            config.sacuvaj(novi)
            prozor.destroy()
            os.execv(sys.executable, [sys.executable] + sys.argv)
        except:
            messagebox.showerror("Greska", "Unesite ispravne brojeve!")

    tk.Button(prozor, text="SACUVAJ I RESTARTUJ",
             command=sacuvaj_i_restartuj,
             bg="#00ff88", fg="#000000",
             font=("Consolas", 10, "bold"),
             width=20).grid(row=5, columnspan=2, pady=15)

    prozor.mainloop()