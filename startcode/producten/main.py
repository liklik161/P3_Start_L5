from product_utils import *
import requests
import schedule
import time
chatnaam = "P3L5"

def verstuur_notificatie(product):
    bericht = f"Nieuw product: {product.titel} en prijs {product.prijs}"
    # requests.post(f"https://ntfy.sh/{chatnaam}",data=f"{bericht}".encode(encoding="utf-8"))
    print(bericht)
def check_producten():
    producten = haal_producten_op_simulatie()
    oude_producten = laad_oude_producten()
    print(f"vorige keer waren er {len(oude_producten)} producten")
    print(f"deze heer zijn het er {len(producten)}")
    for product in producten:
        if product not in oude_producten:
            verstuur_notificatie(product)

    bewaar_producten(producten)

schedule.every(5).minutes.do(check_producten)
while(True):
    schedule.run_pending()
    time.sleep(1)


