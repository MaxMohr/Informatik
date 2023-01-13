import numbers
x = 1           # loop
while True:     # loop

    # Input wird erfragt
    num = int(input("Gib eine Zahl zur Überprüfung ein, ob sie größer oder kleiner als null ist."))

    # Überprüfung ob die Zahl größer als 0 ist
    if num > 0:
        print("Deine Zahl ist größer als 0.")

    # Überprüfung ob die Zahl gleich  0 ist
    elif num==0:
        print("Deine Zahl ist 0.")

    # Überprüfung ob die Zahl kleiner als 0 ist
    elif num < 0:
        print("Deine Zahl ist kleiner als 0.")

    x += 1          # loop