# Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. In simple terms:

# Polymorphism means "many forms" — the same function or method can behave differently depending on the object calling it.


from abc import ABC, abstractmethod

# Define an abstract class

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
# Derived class 1

class Car(Vehicle):
    def start_engine(self):
        return 'Car Enginer started'
    
# Derived class 2

class Motorcycle(vehicle):
    def start_engine(self):
        return 'Motorcycle enginer started'
    
car = Car()
motorcycle = Motorcycle()

start_vehicle(car)


# Polymorphism via inheritance  
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
