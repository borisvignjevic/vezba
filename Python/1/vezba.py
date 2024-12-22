
program_name = "Automobili"
version = 1.0
is_new_program = True
print(program_name, version, is_new_program)
# list -> array , "BMW" "WV" , "Audi",
#          0      1      2
cars = ["BMW", "WV", "Audi"]


print(cars[0])

# Kako promeniti prvu stavku iz liste "BMW" -> "Skoda"

cars[0] = "Skoda"
print(cars)
cars.remove("Audi")
print(cars)