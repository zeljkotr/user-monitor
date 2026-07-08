import pystray
import threading
import settings
import config
from icon import napravi_ikonu

def pokreni_tray(stop_event):
    def otvori_podesavanja(icon, item):
        threading.Thread(
            target=settings.otvori_settings,
            daemon=True
        ).start()

    def izlaz(icon, item):
        stop_event.set()
        icon.stop()

    ikona = napravi_ikonu()

    menu = pystray.Menu(
        pystray.MenuItem("User Monitor v1.0", None, enabled=False),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("⚙️ Podesavanja", otvori_podesavanja),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("❌ Izlaz", izlaz)
    )

    icon = pystray.Icon(
        "user-monitor",
        ikona,
        "User Monitor",
        menu
    )

    icon.run()