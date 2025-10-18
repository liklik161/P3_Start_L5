# Maak een ntfy-notificatie
chatnaam = "P3L5"

import requests

requests.post(f"https://ntfy.sh/{chatnaam}",data="hey".encode(encoding="utf-8"),
              headers= {"Title": "session terminated",
                        "Priority": "5"})