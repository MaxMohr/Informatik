print("Taschenrechner erfolgreich gestartet!")
print()


calculation = input(print("Bitte wähle die Rechenart (+, -, :, *, ^)"))
print()
a = int(input("Was ist deine erste Zahl? "))
b = int(input("Was ist deine zweite Zahl? "))
print()
if calculation=="+":
    ergebnis=a+b
elif calculation=="-":
    ergebnis=a-b
elif calculation==":":
    if b==0:
        ergebnis="Fehler! Division durch 0 nicht möglich!"
    else:
        ergebnis=a/b
elif calculation=="*":
    ergebnis=a*b
elif calculation=="^":
    ergebnis=a**b
else:
    ergebnis=f"Ungültiges Rechenzeichen benutzt: ({calculation})!"

print(f"Dein Ergebnis lautet: {ergebnis}")


'''
Nur addieren noch einfacher

def add(num1, num2):
print(f"{num1} + {num2} = {num1 + num2}")

a = int(input("Gib die 1. Zahl ein"))
b = int(input("Gib die 2. Zahl ein"))
add(a, b)
'''