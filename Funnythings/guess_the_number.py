import random
import time
print()
print(""
      "Guess the number wurde erfolgreich gestartet!"
      "Du hast 3 Versuche die Zahl zu erraten."
      "")
print()

x = 1
while True:

    randomrange = int(input("""Bitte gib die Range der random Zahlen ein! 
(Bei 20 gil, dass Zahlen von 0-20 Die Lösung sein können) """))
    print()

    number = random.randrange(randomrange +1)

    input1 = int(input(f"Errate die Zahl (0-{randomrange})! (1/3)"))
    if input1==number:
        print()
        print("Super! Beim ersten Versuch ")
        time.sleep(3)
        for y in range(10):
            print()
        print("Spiel wird neugestartet!")
        print()
        x += 1

    elif input1!=number:
        print()
        input2 = int(input("Leider falsch! (2/3) "))

        if input2==number:
            print()
            print("Gut gemacht! Beim 2. Versuch ")
            time.sleep(3)
            for y in range(10):
                print()
            print("Spiel wird neugestartet!")
            print()
            x += 1

        elif input2!=number:
            print()
            input3 = int(input("Leider falsch! (3/3) "))

            if input3==number:
                print()
                print("Bravo. Gerade noch geschafft! ")
                time.sleep(3)
                for y in range(10):
                    print()
                print("Spiel wird neugestartet!")
                print()
                x += 1


            elif input3!=number:
                print()
                print(f"Auch diese Zahl ist leider falsch! Die Zahl war: {number}")
                time.sleep(3)
                for y in range(10):
                    print()
                print("Spiel wird neugestartet!")
                print()
    x+=1
