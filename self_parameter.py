class Car:
    def __init__(self):
        self.car_brand = None
        self.horse_power = None
        self.color = None
        # __init__ ist eine spezielle Methode, die automatisch aufgerufen wird, wenn ein neues Objekt der Klasse erstellt wird. Sie dient dazu, die Attribute des Objekts zu initialisieren. In diesem Fall werden die Attribute car_brand, horse_power und color auf None gesetzt, was bedeutet, dass sie noch keinen Wert haben.
        # methoden sind Funktionen, die innerhalb einer Klasse definiert sind und auf die Attribute der Klasse zugreifen können. Sie können verwendet werden, um das Verhalten von Objekten zu definieren.
        #self ist ein spezielles Schlüsselwort in Python, das innerhalb einer Klasse verwendet wird, um auf die Instanz der Klasse zuzugreifen. Es ermöglicht es, die Attribute und Methoden der Klasse zu referenzieren und zu manipulieren. In diesem Fall wird self verwendet, um die Attribute car_brand, horse_power und color zu definieren und zu initialisieren.

car1 =Car()       
print(car1.car_brand)
car1.car_brand = "BMW"
print(car1.car_brand)
car1.horse_power = 150
print(car1.horse_power)
car1.color = "schwarz"
print(car1.color)

car2 =Car()       
print(car2.car_brand)
car2.car_brand = "audi"
print(car2.car_brand)
car1.horse_power = 180
print(car2.horse_power)
car1.color = "blau"
print(car2.color)

# car1 ist ein Objekt der Klasse Car. Durch die Verwendung von car1.car_brand greifen
# man kann mehrere Objekte der Klasse Car erstellen, wie car2, und jedes Objekt hat seine eigenen Attribute. In diesem Beispiel hat car1 die Marke "BMW", während car2 die Marke "audi" hat. Die Attribute horse_power und color werden ebenfalls für jedes Objekt separat festgelegt.

