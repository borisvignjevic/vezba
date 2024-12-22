
name = "admin"
name = name.lower() # "ToMa" -> "toma"

# ako je ime admin        -> if
# ako je ime toma         -> elif
# ako je bilo koje drugo ime -> else


if name == "admin":
    print("Dobrodosao admine")
elif name == "toma":
    print("Dobrodosao Tomo")
else:
    print("Dobro dosao neko drugi")



