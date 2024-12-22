
cars = ["Audi","BMW","Zastava"]


print(cars)

# BMW -> Mercedes
cars[1] = "Mercedes"
print(cars)

# Dodati jos 1 automobil na kraju "Skoda
cars.append("Skoda")
print(cars)

# Sortirajte cars A-Z
cars.sort()
print(cars)

# Trntno na stanju imamo x automobila
print(f"Trenutno na stanju imamo {len(cars)} automobila")
