import psutil
import time
from datetime import datetime
import config
import alerts

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

def uzmi_chrome_resurse():
    cpu_ukupno = 0
    ram_ukupno = 0
    for p in psutil.process_iter(["name", "cpu_percent", "memory_percent"]):
        try:
            if p.info["name"] and "chrome" in p.info["name"].lower():
                cpu_ukupno += p.info["cpu_percent"]
                ram_ukupno += p.info["memory_percent"]
        except:
            pass
    return round(cpu_ukupno, 1), round(ram_ukupno, 1)

def uzmi_ivms_resurse():
    cpu_ukupno = 0
    ram_ukupno = 0
    procesi = 0
    for p in psutil.process_iter(["name", "cpu_percent", "memory_percent"]):
        try:
            if p.info["name"] and "ivms-4200" in p.info["name"].lower():
                cpu_ukupno += p.info["cpu_percent"]
                ram_ukupno += p.info["memory_percent"]
                procesi += 1
        except:
            pass
    return round(cpu_ukupno, 1), round(ram_ukupno, 1), procesi

def uzmi_ivms_mrezu():
    try:
        ivms_procesi = [p for p in psutil.process_iter(["name", "pid"])
                       if p.info["name"] and "ivms-4200" in p.info["name"].lower()]

        ukupno_mreza = psutil.net_io_counters()
        ukupno_bytes = ukupno_mreza.bytes_sent + ukupno_mreza.bytes_recv

        ivms_bytes = 0
        for p in ivms_procesi:
            try:
                io = p.io_counters()
                ivms_bytes += io.read_bytes + io.write_bytes
            except:
                pass

        if ukupno_bytes > 0:
            procenat = round((ivms_bytes / ukupno_bytes) * 100, 1)
        else:
            procenat = 0

        return procenat
    except:
        return 0

def proveri():
    cpu = uzmi_cpu()
    ram = uzmi_ram()
    mreza = uzmi_mrezu()
    chrome_cpu, chrome_ram = uzmi_chrome_resurse()
    ivms_cpu, ivms_ram, ivms_procesi = uzmi_ivms_resurse()
    ivms_mreza = uzmi_ivms_mrezu()

    log(f"CPU: {cpu}% | RAM: {ram}% | Mreza: {mreza} MB/s | "
        f"Chrome CPU: {chrome_cpu}% RAM: {chrome_ram}% | "
        f"iVMS CPU: {ivms_cpu}% RAM: {ivms_ram}% "
        f"Procesi: {ivms_procesi} Mreza: {ivms_mreza}%")

    if cpu > config.CPU_PRAG:
        alerts.upozori("cpu", config.PORUKE["cpu"])
    else:
        alerts.ocisti("cpu")

    if ram > config.RAM_PRAG:
        alerts.upozori("ram", config.PORUKE["ram"])
    else:
        alerts.ocisti("ram")

    if mreza > config.MREZA_PRAG_MB:
        alerts.upozori("mreza", config.PORUKE["mreza"])
    else:
        alerts.ocisti("mreza")

    if chrome_cpu > 50:
        alerts.upozori("chrome_cpu", "Chrome trosi previse CPU! Zatvorite tabove.")
    else:
        alerts.ocisti("chrome_cpu")

    if chrome_ram > 50:
        alerts.upozori("chrome_ram", "Chrome trosi previse RAM! Zatvorite tabove.")
    else:
        alerts.ocisti("chrome_ram")

    if ivms_cpu > 50:
        alerts.upozori("ivms_cpu",
            "iVMS-4200 usporava racunar!\n\n"
            "Resenje:\n"
            "1. Smanjite broj kamera na ekranu\n"
            "2. Zatvorite iVMS ako nije potreban")
    else:
        alerts.ocisti("ivms_cpu")

    if ivms_ram > 30:
        alerts.upozori("ivms_ram",
            "iVMS-4200 trosi previse memorije!\n\n"
            "Resenje:\n"
            "1. Restartujte iVMS\n"
            "2. Smanjite broj aktivnih kamera")
    else:
        alerts.ocisti("ivms_ram")

    if ivms_mreza > 50:
        alerts.upozori("ivms_mreza",
            "iVMS-4200 trosi previse mreze!\n\n"
            "Resenje:\n"
            "1. Smanjite broj kamera na ekranu\n"
            "2. Zatvorite iVMS ako nije potreban")
    else:
        alerts.ocisti("ivms_mreza")

if __name__ == "__main__":
    log("=" * 50)
    log("POKRECEM USER MONITOR")
    log("=" * 50)

    while True:
        try:
            proveri()
        except Exception as e:
            log(f"GRESKA: {e}")
        time.sleep(config.INTERVAL)