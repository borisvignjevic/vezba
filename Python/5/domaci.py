
# Pitati korisnika da unese ime proizvoda
# Kada unese ime proizvoda dodati proizvod i "kasu"
# Korisnik mora unati 3 proizvoda

register = list()

# Dok kod broj stavki u register je manji od 3 pitaj korisnika da unese novi
# kad korisnik unese novi dodati ga u registar

while len(register) <3:
    item = input("Unesite ime proizvoda")
    register.append(item)
    print(register)


