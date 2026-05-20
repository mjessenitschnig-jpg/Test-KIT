test_variable = 10
# Variablen können nur einen wert speichern
numbers = [3, 5, 15, 17, 20]
# Listen können mehrere Werte speichern

print(type(numbers))



names = ["Max", "Moritz", "Lisa", "Anna"]
# kann auch mit Strings arbeiten
print(names)

print(names[1])
# in der eckigen klammer wir der index angegeben, der bei 0 beginnt
# also gibt names[1] den 2. Eintrag der Liste zurück, in diesem Fall "Moritz"

print(names[-1])
# mit negativen indices kann auf die Elemente von hinten zugegriffen werden
# names[-1] gibt den letzten Eintrag der Liste zurück, in diesem Fall "Anna"

names[0] = "Tom"
# Listen sind veränderbar, das heißt man kann die Werte in einer Liste ändern
print(names)
