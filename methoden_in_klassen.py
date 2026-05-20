class Car:
    def __init__(self):
        self.car_brand = None
        self.horse_power = None
        self.color = None
        self.x_position = 5
        self.y_position = 5

        # __init__ ist eine spezielle Methode, die automatisch aufgerufen wird, wenn ein neues Objekt der Klasse erstellt wird. Sie dient dazu, die Attribute des Objekts zu initialisieren. In diesem Fall werden die Attribute car_brand, horse_power und color auf None gesetzt, was bedeutet, dass sie noch keinen Wert haben.
        # methoden sind Funktionen, die innerhalb einer Klasse definiert sind und auf die Attribute der Klasse zugreifen können. Sie können verwendet werden, um das Verhalten von Objekten zu definieren.
        #self ist ein spezielles Schlüsselwort in Python, das innerhalb einer Klasse verwendet wird, um auf die Instanz der Klasse zuzugreifen. Es ermöglicht es, die Attribute und Methoden der Klasse zu referenzieren und zu manipulieren. In diesem Fall wird self verwendet, um die Attribute car_brand, horse_power und color zu definieren und zu initialisieren.
    def drive(self, x, y):
        self.x_position += x
        self.y_position += y
        print(f"Das Auto fährt zu Position ({self.x_position}, {self.y_position})")
      # die Methode drive nimmt zwei Parameter x und y entgegen, die die Anzahl der Schritte angeben, die das Auto in x- und y-Richtung fahren soll. Die Methode aktualisiert die x_position und y_position des Autos entsprechend und gibt die neue Position aus.  

car1 =Car()     
print(car1.x_position)
print(car1.y_position)  
car1.drive(5, 10)
print(car1.x_position)
print(car1.y_position)
