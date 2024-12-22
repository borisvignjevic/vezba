import loca

from vezba7 import allowed_options, highest_price, most_expensive_product

products = {
    "hleb" : {
        "cena" : 150,
        "kolicina": 50
    },
    "pivo" : {
        "cena": 200,
        "kolicina" : 100
    },
    "jagode" : {
        "cena": 300,
        "kolicina" : 600
    }
}

allowed_options = [
    "dodaj", "obrisi","izlistaj"
    "stop", "istorijat","obrisi sve",
    "prikazi naj skuplji proizvod", "pnp"
]

option = None
history = []

while option not in allowed_options:
    option = input(f"Sta zelite da uraite? {",".join(allowed_options)} \n").lower()

    if  option == "obrisi" :
        product = None

        while product not in products:
            product = input("Unesite ime proizvoda za brisanje: \n").lower()

            del products[product]

            msg = f"Obrisali ste {product} \n"
            print(msg)
            history.append(msg)
            options = None

    elif option == "dodaj" :

         product = None

         while product in products or product == None:
             product = input("Unesite ime proizvoda koji nepostoji: \n")

         product_price = None
         while product_price is None or product_price <=0:
             product_price = int(input("Unesite cenu proizvoda: \n"))
         product_amount = None
         while product_amount is None or product_amount < 0:
             product_amount = int(input("Unesite kolicinu proizvoda: \n"))


         products[product] = {
               "cena" : product,
               "kolicina" : product_amount
         }
         option = None
         msg = f"Dodali ste proizvod {product} \n"
         print(msg)
         history.append(msg)

    elif option == "dodaj":

        product = None

        while product in products or product == None:
            product = input("Unesite ime proizvoda koji ne postoji \n")

        product_price = None
        while product_price is None or product_price <= 0:
            product_price = int(input("Unesite cenu proizvoda: \n"))
        product_amount = None
        while product_amount is None or product_amount <= 0:
            product_amount = int(input("Unesite kolicinu proizvoda: \n"))



        products[product] = {
            "cena" : product,
            "kolicina" : product_amount
        }
        option = None

        msg = f"Dodali ste novi proizvod{product} \n"
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

    elif option == " najskuplji proizvod" or "pnp":

        highest_price = 0
        most_expensive_product = None

        for product in products:
            if highest_price < products[product]['cena']:
                highest_price = products[product]['cena']
                most_expensive_product = product

        print(products[most_expensive_product]['cena'])

print(products)




