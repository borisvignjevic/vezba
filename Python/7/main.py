
products = {
    "hleb":{
        "cena": 100,
        "kolicina" : 50
    },
    "pivo":{
        "cena" : 150,
        "kolicina" : 220
    }
}
print(products)

option = None

while option not in ["dodaj", "obrisi"]:
    option = input("Sta zelite da odradite?[dodaj,obrisi]").lower()

if option == "obrisi":
    product = None

    while product not in products:
        product = input("Uneite ime proizvoda za brisanje: ").lower()

    del products[product]

elif option == "dodaj":

    product = None

    while product in products or product == None:
        product = input("Unesite ime proizvoda koji ne postoji")

    productPrice = None
    while productPrice == None or productPrice <= 0:
        productPrice = int(input("Unesite cenu proizvoda: "))

    productAmount = None
    while productAmount == None or productAmount < 0:
        productAmount = int(input("Unesite kolicinu proizvoda: "))


    print(product, productPrice, productAmount)

    products[product] = {
        "cena": productPrice,
        "kolicina" : productAmount
    }

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