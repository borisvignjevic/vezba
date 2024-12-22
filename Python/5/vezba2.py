
# pitaj korisnika koliko godina ima
# ako nije uneo pitaj opet


age = ""

while not age.isdigit() or int(age) < 18:
    age = input("koliko godina imate?")

    print(age)