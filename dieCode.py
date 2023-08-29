# Imports
import csv
from datetime import date

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
import csv
from datetime import date

# Functie om producten te verkopen.
def product_verkopen(productnaam):
    global ingekochte_producten, verkochte_producten
    today = date.today()
    
    for product in ingekochte_producten:
        if product[0] == productnaam:
            if product[1] > 0:
                if today <= date.fromisoformat(product[3]):
                    product[1] -= 1
                    print(f"{productnaam} is verkocht. Nieuwe voorraad: {product[1]}")
                    verkoopdatum = today
                    product.append(verkoopdatum.strftime('%Y-%m-%d'))
                    print(f"Verkoopdatum: {product[-1]}")
                    # Update de verkochte_producten lijst
                    for verkocht_product in verkochte_producten:
                        if verkocht_product[0] == productnaam:
                            verkocht_product[2] = verkoopdatum.strftime('%Y-%m-%d')
                else:
                    print(f"Sorry, {productnaam} verkopen wij niet meer. Houdbaarheidsdatum verstreken.")
                    product[1] = 0
            else:
                print(f"Sorry, {productnaam} is helaas uitverkocht.")
    
    # Aanpassen van de verkochte_producten lijst
    for verkocht_product in verkochte_producten:
        if verkocht_product[0] == productnaam:
            verkocht_product[2] = today.strftime('%Y-%m-%d')
            print(f"Verkocht product: {verkocht_product}")

# De ingekochte producten.
ingekochte_producten = [
    ["product_naam", "voorraad", "inkoopprijs", "houdbaarheidsdatum"],
    ["appelsap", 30, 2, "2023-09-05"],
    ["muffin", 28, 1, "2023-10-14"],
    ["appelstroop", 7, 2, "2024-01-01"],
    ["marshmallow", 580, 1, "2023-11-05"]
]

# Naam van het CSV-bestand voor ingekochte producten.
ingekochte_csv = "ingekochte_producten.csv"

# CSV-bestand openen voor schrijven.
with open(ingekochte_csv, mode='w', newline='') as inkoop:
    schrijver = csv.writer(inkoop)
    schrijver.writerows(ingekochte_producten)

# Datum van vandaag definiëren
today = date.today()

# Verkochte producten.
verkochte_producten = [
    ["product_naam", "verkoopprijs", "verkoopdatum"],
    ["appelsap", 3, ""],
    ["muffin", 5, ""],
    ["appelstroop", 6, ""],
    ["marshmallow", 2, ""]
]

# Naam van het CSV-bestand voor verkochte producten.
verkochte_csv = "verkochte_producten.csv"

# CSV-bestand openen voor schrijven.
with open(verkochte_csv, mode='w', newline='') as verkoop:
    schrijver = csv.writer(verkoop)
    schrijver.writerows(verkochte_producten)

# producten verkopen:
product_verkopen("marshmallow")
product_verkopen("appelstroop")
product_verkopen("marshmallow")

# De verkochte_producten lijst na elk verkocht product.
print(verkochte_producten)