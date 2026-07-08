import psutil
import time
import threading
from datetime import datetime
import config
import alerts
import tray

stop_event = threading.Event()

def log(poruka):
    vreme = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linija = f"{vreme} | {poruka}"
    print(linija)
    with open(config.LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linija + "\n")

def uzmi_cpu():
    return psutil.cpu_percent(interval=1)

def uzmi_ram():
    return psutil.virtual_memory().percent

def uzmi_mrezu():
    pre = psutil.net_io_counters()
    time.sleep(1)
    posle = psutil.net_io_counters()
    bytes_sec = (posle.bytes_sent + posle.bytes_recv) - (pre.bytes_sent + pre.bytes_recv)
    return round(bytes_sec / (1024**2), 2)

def uzmi_top_program(resurs="cpu"):
    programi = {}
    for p in psutil.process_iter(["name", "cpu_percent", "memory_percent"]):
        try:
            ime = p.info["name"]
            if not ime:
                continue
            if "chrome" in ime.lower():
                ime = "Google Chrome"
            elif "ivms-4200" in ime.lower():
                ime = "iVMS-4200"
            vrednost = p.info["cpu_percent"] if resurs == "cpu" else p.info["memory_percent"]
            if ime in programi:
                programi[ime] += vrednost
            else:
                programi[ime] = vrednost
        except:
            pass

    if not programi:
        return "Nepoznat", 0

    top = max(programi, key=programi.get)
    return top, round(programi[top], 1)

def poruka_za_program(ime):
    if ime == "Google Chrome":
        return "Zatvorite nepotrebne tabove u Chrome-u."
    elif ime == "iVMS-4200":
        return "Smanjite broj kamera na ekranu ili zatvorite iVMS."
    else:
        return f"Zatvorite {ime} ako nije potreban."

def proveri():
    cfg = config.ucitaj()
    cpu = uzmi_cpu()
    ram = uzmi_ram()
    mreza = uzmi_mrezu()

    log(f"CPU: {cpu}% | RAM: {ram}% | Mreza: {mreza} MB/s")

    if cpu > cfg["CPU_PRAG"]:
        top_ime, top_vrednost = uzmi_top_program("cpu")
        alerts.upozori("cpu",
            f"CPU je preopterecen! ({cpu}%)\n\n"
            f"Krivac: {top_ime} ({top_vrednost}%)\n\n"
            f"{poruka_za_program(top_ime)}")
    else:
        alerts.ocisti("cpu")

    if ram > cfg["RAM_PRAG"]:
        top_ime, top_vrednost = uzmi_top_program("ram")
        alerts.upozori("ram",
            f"Memorija je preopterecena! ({ram}%)\n\n"
            f"Krivac: {top_ime} ({top_vrednost}%)\n\n"
            f"{poruka_za_program(top_ime)}")
    else:
        alerts.ocisti("ram")

    if mreza > cfg["MREZA_PRAG_MB"]:
        alerts.upozori("mreza",
            f"Mreza je zasicena! ({mreza} MB/s)\n\n"
            f"Proverite da li neko preuzima velike fajlove\n"
            f"ili ima previse kamera otvorenih u iVMS-u.")
    else:
        alerts.ocisti("mreza")

if __name__ == "__main__":
    alerts.splash()

    # Pokreni tray u posebnom threadu
    tray_thread = threading.Thread(
        target=tray.pokreni_tray,
        args=(stop_event,),
        daemon=True
    )
    tray_thread.start()

    log("=" * 50)
    log("POKRECEM USER MONITOR")
    log("=" * 50)

    while not stop_event.is_set():
        try:
            proveri()
        except Exception as e:
            log(f"GRESKA: {e}")
        time.sleep(config.INTERVAL)