print("Willkommen zum Lotto-Spiel!")
number1 = int(input("Bitte wähle eine Zahl zwischen 1 und 49:"))
number2 = int(input("Bitte wähle eine Zahl zwischen 1 und 49:"))
number3 = int(input("Bitte wähle eine Zahl zwischen 1 und 49:"))

# Gewinnzahl 1: 3
# Gewinnzahl 2: 14
# Gewinnzahl 3: 22
# Hier unten sieht man das beispiel für if verschachtelungen jedes if braucht auch ein else, damit es funktioniert. zu kompliziert 
if number1 == 3:
    if number2 == 14:
        if number3 == 22:
            print("Herzlichen Glückwunsch! Sie haben den Jackpot gewonnen!")
        else:
            print("Du hast leider verloren . . . ")
    else:
        print("Du hast leider verloren . . . ")
else:
    print("Du hast leider verloren . . . ")
# hier das besssere Beispiel für if verschachtelungen, da es übersichtlicher ist, mit and funktion. gibt auch or oder not funktion, aber die sind hier nicht nötig. 
if number1 == 3 and number2 == 14 and number3 == 22:
    print("Herzlichen Glückwunsch! Sie haben den Jackpot gewonnen!")
else:
    print("Du hast leider verloren . . . ")

