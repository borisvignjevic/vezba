

# Conditional statment / Uslovi/ Kondicionali -> Ifovi :)

# poslednji klik = "navigacija"
# ako je poslednji_klik  navigacija onda prikazi padajuci meni

# kategorija, ako je kategorija "frizider", prikazi frizidere

name = "Toma"

# ako je ime Toma -> ispis poruku "Pozdrav Tomo"
#Ako je ime neko drugo (ako nije Toma) ispisi "Pozdrav neko drugi"

# if (ako) name (je ime) == (ako je njegova vrednost) "Toma"
# ako je name "Toma"

if name == "Toma":
        print("Pozdrav Tomo!")
        print("Pozdrav drugi put!")
else:
        print("Pozdrav neko drugi!")

age = 31

# uraditi proveru, ako korisnik ima vise od 18 godina ispisati "Punoletni ste"
# ako korisnik ima manje od 18 godina ispisati "Niste Punoletni"

if age >=18:
    print("Punoltni ste")
else:
    print("Niste punoletni")