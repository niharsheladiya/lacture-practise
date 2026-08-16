# Python OOP Examples

# Class definition

# A class is a blueprint or template used to create objects.
# It defined what data and actions an object will have.abs
# Data : Attributed
# Actions : Methods

# House Bluperint

# Class = Blueprint / Design

# Object defination

# An object is a real instance of a class.

# It contains actual values and can use the methods defined in the class.abs

# Blueprint -> Honda , Audi, Tesla

# Object : Real thing

# Encapsulations

# Encpsulation means keeping data and methods together inside a class and protecting important data from direct access.

# ATM Machine -> Withdraw Cash -> Deposit Case

# Encapsulation = Data Protection +  Controlled Access


'''
class ClassName:
  pass

car = className()

1. Attributes
2. Constructor
3. Destructor
4. self keyword
'''

class Car:

    #constructor

    def __init__(self , brand=None , model=None , color=None , price=None , name=None , age=None , dob=None , marks=None):

        #car

        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

        #user

        self.name = name
        self.age = age
        self.dob = dob
        self.marks = marks


    #method

    def start(self):
      print(f"{self.brand} {self.model} is Starting....")


    #method

    def Car_Details(self):
      print(f"""
      Brand : {self.brand}
      Model : {self.model}
      Color : {self.color}
      Price : {self.price}
      """)


    def User_Details(self):
      print(f"""
      Name : {self.name}
      Age : {self.age}
      DOB : {self.dob}
      Marks : {self.marks}
      """)

car1 = Car("BMW" , "M5 COM" , "Black" , "50000000" , "Nihar" , 18 , "15-06-2008" , 100)

car1.Car_Details()


class Student:

  #constructor

  def __init__(self , name=None , age=None , dob=None , marks=None):

      #user
      self.name = name
      self.age = age
      self.dob = dob
      self.marks = marks


  def User_Details(self):
      print(f"""
      Name : {self.name}
      Age : {self.age}
      DOB : {self.dob}
      Marks : {self.marks}
      """)

student1 = Student("Nihar" , 18 , "15-06-2008" , 100)

student1.User_Details()


#Simple Creation

class Person:

    pass

p1 = Person()

print(type(p1))


class Person:

    name = "Nihar"

    age = 18

    course = "Python"

p1 = Person()

print(p1.name)
print(p1.age)
print(p1.course)
      
      












        
