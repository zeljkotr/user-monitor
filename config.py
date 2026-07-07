# Pragovi za upozorenja
CPU_PRAG = 90
RAM_PRAG = 90
MREZA_PRAG_MB = 100    # MB/s — kad predje ovo, mreza je zasicena
CHROME_TABOVI_PRAG = 15  # broj Chrome procesa

# Interval provere u sekundama
INTERVAL = 5

# Log fajl
LOG_FILE = "C:\\vezbe\\user-monitor\\monitor.log"

# Poruke upozorenja
PORUKE = {
    "cpu": "⚠️ Procesor je preopterecen! Zatvorite nepotrebne programe.",
    "ram": "⚠️ RAM je skoro pun! Zatvorite nepotrebne programe.",
    "mreza": "⚠️ Mreza je zasicena! Iskljucite program za kamere ako nije potreban.",
    "chrome": "⚠️ Previse Chrome tabova! Zatvorite neke tabove."
}