

# korisnik treba da unese cenu korpe
# ako je cena preko 1000 ispisati koliki popust su ostvarili (10%) 1000 "Ostvarili ste popust sto iznosi 100
# Ako je cena ispod 1000 ispisati "Vasa korpa iznosi 1000"

# DONE: imam cenu  i proveru da li je preko 1000 ili manja
# DONE: Pitam korisnika za price (input)
# DONE: Racunam porez
# DONE: Promeniti poruku koja se ispisuje
# DONE: Revidiram kod i gledam da li to moze  bolje



price = 500

price = int(input("Unesite cenu korpe"))

if price >= 1000:
    tax_amaunt = price*0.10
    print(f"Ostarili ste 10% popusta sto ukupno iznosi  {tax_amaunt} eura")
else:
    print("Cena je manja od 1000")