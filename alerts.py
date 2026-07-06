import ctypes
import threading
from datetime import datetime

# Pamti koja upozorenja su vec prikazana
vec_prikazano = set()

def popup(naslov, poruka):
    # Windows MessageBox — iskace na ekranu
    ctypes.windll.user32.MessageBoxW(0, poruka, naslov, 0x30)

def upozori(tip, poruka):
    if tip not in vec_prikazano:
        vec_prikazano.add(tip)
        # Pokreni popup u posebnom threadu da ne blokira monitoring
        t = threading.Thread(target=popup, args=(f"⚠️ UPOZORENJE", poruka))
        t.daemon = True
        t.start()
        
        vreme = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{vreme} | ALERT: {poruka}")

def ocisti(tip):
    vec_prikazano.discard(tip)