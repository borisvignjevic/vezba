
tajni_pin = 3124


# ako je tajni pin 4231 ILI ako je tajni pin 3124 ispisati poruku "PIN JE TACAN"
# u suprotnom izbaciti poruku "NETACAN PIN!"
# Zabranjeno koriscenje vise od 1 IF-a i zabranjeno koriscenje elif
# Dozvoljeno 1 If + 1 else

if tajni_pin == 4231 or tajni_pin == 3124:
    print("Pin je tacan!")
else:
    print("Pin je netacan")