
cities = ["Beograd", "Novi Sad", "Nis", "Kragujevac"]



def price_beograd():
    return 1000  # Primer cena

def price_novisad():
    return 2000  # Primer cena

def price_nis():
    return 1500  # Primer cena

# Skladištimo funkcije u rečnik (ili listu)
price = {
    "beograd": cena,
    "novi sad": cena,
    "nis": cena
}

# Petlja za pozivanje funkcija i prikaz cena
for naziv, funkcija in funkcije_cene.items():
    cena = funkcija()  # Pozivanje funkcije
    print(f"{naziv}: {cena} RSD")