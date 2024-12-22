
# Napisite program koji trazi od korisnika da unese ime proizvoda, a zatim ispisuje cenu tog proizvoda
# Ako proizvod ne postoji ispisati poruku "Proizvod nije pronadjen"

products = {"iphone 14": 999, "iphone 15": 1200, "samsung s23": 1300}
search_product = input("Unesite ime proizvoda:").lower()

if search_product in products:
    print(products[search_product])
else:
    print("Proizvod nije pornadjen")