# Abstraction

# Abstraction mean Hiding Implementation details and showing only important features.


from abc import ABC , abstractmethod
import math

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car starting!!!!......")


class Bike(Vehicle):

    def start(self):
        print("Bike starting....!!!")

c = Car()
b = Bike()

c.start()
b.start()


print("========== Q.1 ===========")

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Reactangle(Shape):

    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


try:


    s = Shape()
except TypeError as e:
    print("Shape Error:"  , e)

r = Reactangle(10 , 20)

print("Rectangle Area:" , r.area())


c = Circle(7)

print(f"Circle Area : {c.area():.3f}" , )

print(f"Circle Area : round(c.area() , 2)")
























    
