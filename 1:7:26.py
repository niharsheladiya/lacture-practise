#Python oop example

#Class defination

#A class is a blueprint or template used to create objects
#It defined what data and action an object will have.ads
#Data:Attributed
#Actions:Methods

#House Blueprint

#Class = Blueprint/Design

# Object defination

# An object is a real instance of a class.

# It contains actual values and can use the methods defined in the class.abs

# Blueprint -> Honda , Audi, Tesla

# Object : Real thing

# Encapsulations

# Encpsulation means keeping data and methods together inside a class and protecting important data from direct access.

# ATM Machine -> Withdraw Cash -> Deposit Case

# Encapsulation = Data Protection +  Controlled Access


class ClassName:
  pass

car = className()

1.Attributes
2.Constuctor
3.Destuctor
4.self keyword

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
    print(f"{self.brand} {self.model} is Starting.......")


  #method

  def Car































      
