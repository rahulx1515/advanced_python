### Class and Object Basics in OOP

## Class:
# A class is a blueprint or template that defines the properties (attributes) and behaviors (methods) that 
# the objects created from the class can have. It acts as a framework for creating multiple similar objects.

## Object:
# An object is an instance of a class. It is a specific realization of the blueprint defined by the class, 
# holding real values for the properties and capable of performing the actions defined in the class.

class Car:
    def __init__(self, brand, color, max_speed):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed

    def start(self):
        return f"The {self.color} {self.brand} starts."

    def stop(self):
        return f"The {self.color} {self.brand} stops."

car1 = Car("Toyota", "Red", 180)
car2 = Car("Honda", "Blue", 200)

print(car1.start())  
print(car2.stop())   
