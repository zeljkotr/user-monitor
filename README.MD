# 🖥️ User Monitor

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-green)

Automatski monitor resursa za Windows — prati CPU, RAM, mrežu i specifične aplikacije u pozadini i upozorava korisnika popup porukom kada pređu definisane pragove.

## ✅ Šta prati
- CPU i RAM sistema
- Mrežni saobraćaj
- **Google Chrome** — upozorava kad troši previše CPU/RAM
- **iVMS-4200** — upozorava kad troši previše CPU, RAM ili mreže

## 🚨 Kako upozorava
Kada resurs predje definisani prag, korisniku iskače **popup poruka** na ekranu sa konkretnim uputstvom šta da uradi.

## ⚙️ Konfiguracija
Izmeni `config.py`:
```python
CPU_PRAG = 80        # % CPU sistema
RAM_PRAG = 85        # % RAM sistema
MREZA_PRAG_MB = 50   # MB/s mreze
INTERVAL = 10        # sekundi između provera
```

## 🚀 Pokretanje
```bash
pip install psutil
python monitor.py
```

## 📦 Windows Binary
Skinite gotov `.exe` iz [Releases](../../releases) ili [Actions Artifacts](../../actions) — ne zahteva instalaciju Pythona.

## 🛠️ Tehnologije
- Python 3
- psutil — monitoring resursa
- ctypes — Windows popup poruke
- PyInstaller — Windows binary
- GitHub Actions — automatski build