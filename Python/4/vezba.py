
# Pitati korisnika za godine
# Ako ima 18 ili vise godina ispisati "Punoletni ste"
# Ako ima manje od 18 ispisati maloletni ste

age = int(input("Unesite vase godine"))

# Ako korisnik ima 12 ili manje godina ispisati "vi ste dete"
# Ako korisnik ima 13 do 18 godina ispisati "vi ste tinejdzer"
#  Ako korisnik ima 18 65 godina ispisati "vi ste odrasla osoba"
# Ako korisnik ima 65 ili vise godina ispisati "vi ste penzioner"
if age < 0 :
    print("godine ne mogu biti manje od 0")
    quit()

if age <= 12:
    print("Vi ste dete")
elif age >= 13 and age < 18 :
    print("Vi ste tinejdzer")
elif age >= 18 and age < 65:
    print("vi ste odrasla osoba")
elif age > 65:
    print("Vi ste penzioner")
