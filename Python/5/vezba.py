
# Napiste petlju brojeve od 0 do 100

numbers = range(100)

for number in range(100):

    if number == 10:
        continue
    if number == 44:
        break

    if number%2 == 0:
        print(f"broj je paran {number}")

# liste korisnika koji ima aktivnu clanarinu
#