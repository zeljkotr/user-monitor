# Pragovi za upozorenja
CPU_PRAG = 85
RAM_PRAG = 80
MREZA_PRAG_MB = 50      # MB/s — kad predje ovo, mreza je zasicena
CHROME_TABOVI_PRAG = 15  # broj Chrome procesa

# Interval provere u sekundama
INTERVAL = 10

# Log fajl
LOG_FILE = "C:\\vezbe\\user-monitor\\monitor.log"

# Poruke upozorenja
PORUKE = {
    "cpu": "⚠️ CPU je preopterecen! Zatvorite nepotrebne programe.",
    "ram": "⚠️ RAM je skoro pun! Zatvorite nepotrebne programe.",
    "mreza": "⚠️ Mreza je zasicena! Iskljucite program za kamere.",
    "chrome": "⚠️ Previse Chrome tabova! Zatvorite neke tabove."
}