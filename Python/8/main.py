
products = {
    "hleb":{
        "cena": 100,
        "kolicina" : 50
    },
    "pivo":{
        "cena" : 150,
        "kolicina" : 220
    },
    "jagode" :{
        "cena" : 120,
        "kolicina" : 22
    }
}

# Izlistaj -> print

# Opcija: STOP

allowed_options = [
    "dodaj", "obrisi", "izlistaj",
    "stop", "istorijat","obrisi sve",
    "prikazi najskuplji proizvod","pnp"
]

# Prikazi najskuplji proizvod
# Napraviti novu opciju: istorijat -> sve sta se desilo!
# Dodali ste novi proizvod IME
# Dodali ste novi proizvod IME
# Dodali ste novi proizvod IME
# Obisali ste IME

option = None
history = []

while option not in allowed_options:
    option = input(f"Sta zelite da odradite? {",".join(allowed_options)} \n").lower()
    if option == "obrisi":
         product = None

         while product not in products:
             product = input("Uneite ime proizvoda za brisanje: \n ").lower()

         del products[product]

         msg = f"Obrisali ste {product}\n"
         print(msg)
         history.append(msg)
         option = None

    elif option == "dodaj":

        product = None

        while product in products or product == None:
            product = input("Unesite ime proizvoda koji ne postoji\n")

        product_price = None
        while product_price is None or product_price <= 0:
            product_price = int(input("Unesite cenu proizvoda:\n"))
        product_amount = None
        while product_amount is None or product_amount < 0:
           product_amount = int(input("Unesite kolicinu proizvoda:\n"))




        products[product] = {
            "cena": product_price,
            "kolicina" : product_amount
        }
        option = None

        msg = f"Dodali ste novi proizvod {product} \n"
        print(msg)
        history.append(msg)

    elif option == "izlistaj":
        print(products)
        option = None

    elif option == "istorijat":
        print(history)
        option = None

    elif option == "obrisi sve":
        products = {}
        option = None
    elif option == "najskuplji proizvod" or "pnp":

        highest_price = 0
        most_expensive_product = None

        for product in products:
            if highest_price < products[product]['cena']:
                highest_price = products[product]['cena']
                most_expensive_product = product

        print(products[most_expensive_product]['cena'])



    # Dodaj proizvod
    # Unesite ime proizvoda "mleko"
    #   => da li proizvod vec postoji
    #   => nesme biti prazno , ne sme biti manje od 2 karaktera


print(products)

# Pitati korisnika sta zeli da uradi
# A: Izbrisi proizvode (obrisi) -> Ispisati logiku za brisanje
# B: Dodaj proizvod (dodaj) -> "dodaj"

# -> Pali se program -> Pitati korisnika "Sta zelite da odradite?"
# Obrisi -> Unesite ime proizvoda za brisanje -> brisemo proizvod
# Dodaj -> Unesite ime proizvoda i cenu -> Test