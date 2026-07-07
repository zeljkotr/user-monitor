import json
import os

# Default vrednosti
DEFAULTS = {
    "CPU_PRAG": 80,
    "RAM_PRAG": 85,
    "MREZA_PRAG_MB": 40,
    "INTERVAL": 10
}

CONFIG_FILE = "C:\\vezbe\\user-monitor\\settings.json"
LOG_FILE = "C:\\vezbe\\user-monitor\\monitor.log"

def ucitaj():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return DEFAULTS.copy()

def sacuvaj(podaci):
    with open(CONFIG_FILE, "w") as f:
        json.dump(podaci, f, indent=4)

# Ucitaj podesavanja
_cfg = ucitaj()
CPU_PRAG = _cfg["CPU_PRAG"]
RAM_PRAG = _cfg["RAM_PRAG"]
MREZA_PRAG_MB = _cfg["MREZA_PRAG_MB"]
INTERVAL = _cfg["INTERVAL"]