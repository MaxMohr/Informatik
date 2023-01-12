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
    ergebnis=a/b
elif calculation=="*":
    ergebnis=a*b
elif calculation=="^":
    ergebnis=a**b
else:
    ergebnis=f"Ungültiges Rechenzeichen benutzt: ({calculation})!"

print(f"Dein Ergebnis lautet: {ergebnis}")

# print("Potenzieren:")
# potenzieren = range(1, 10)
# for x in potenzieren:
#    print(f"2^{x} = {2 ** x}")
# print()
#
# print("Mit eigenen Zahlen rechnen: (+)")
# print()
# print("Danke für eure Aufmerksamkeit!")