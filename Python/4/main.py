

# Vezba 1
# Napravit listu proizvoda i ubaciti 3 proizvoda " iPhone 14", "iPhone 15" , "Samsung s23"
# Napraviti proveru koja proverava da li postoji "iPhone 14" u nasoj listi proizvoda

products = ["iPhone 14", "iPhone 15", "Samsung s23"]

search_item = input("unesite ime teleofona koji trazite")
print(search_item)

if search_item in products:
    print("Pronasli smo telefon")
else:
    print("Nismo pronasli trazeni proizvod")