import json
import os

STARTUP = os.path.join(os.environ["APPDATA"],
          "Microsoft", "Windows", "Start Menu",
          "Programs", "Startup")

CONFIG_FILE = os.path.join(STARTUP, "settings.json")
LOG_FILE = os.path.join(STARTUP, "monitor.log")

DEFAULTS = {
    "CPU_PRAG": 80,
    "RAM_PRAG": 85,
    "MREZA_PRAG_MB": 40,
    "INTERVAL": 10
}

def ucitaj():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            return DEFAULTS.copy()
    return DEFAULTS.copy()

def sacuvaj(podaci):
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(podaci, f, indent=4)

_cfg = ucitaj()
CPU_PRAG = _cfg["CPU_PRAG"]
RAM_PRAG = _cfg["RAM_PRAG"]
MREZA_PRAG_MB = _cfg["MREZA_PRAG_MB"]
INTERVAL = _cfg["INTERVAL"]