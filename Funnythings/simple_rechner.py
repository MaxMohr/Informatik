print("Taschenrechner erfolgreich gestartet!")
print()

# Rechenart wird erfragt
calculation = input(print("Bitte wähle die Rechenart (+, -, :, *, ^)"))
print()

# Zahlen werden erfragt
a = int(input("Was ist deine erste Zahl? "))
b = int(input("Was ist deine zweite Zahl? "))
print()

# Zahlen werden überprüft und ausgerechnet
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

# Ergebnis wird ausgegeben
print(f"Dein Ergebnis lautet: {ergebnis}")


# TODO: funktionsfähig machen
again = input(print("Neue Rechnung starten? (Y/N)"))
if again=="Y":
    def repeat_from_line():
        import inspect
        frame = inspect.currentframe()
        lines = inspect.getframeinfo(frame).code_context
        for line in lines[4:]:
            exec(line)

else:
    print()
    print("Taschenrechner wurde beendet!")

'''
Nur addieren noch einfacher

def add(num1, num2):
print(f"{num1} + {num2} = {num1 + num2}")

a = int(input("Gib die 1. Zahl ein"))
b = int(input("Gib die 2. Zahl ein"))
add(a, b)
'''