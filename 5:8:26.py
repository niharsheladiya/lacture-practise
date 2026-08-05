#Ingeritance oop in python
#1. Single Inheritance

class Parent:

    def display(self):
        print("I am  Parent Class.")

class Child(Parent):

    def show(self):
        print("I am Child Class.")

c1 = Child()


c1.display()
c1.show()



#2. Multiple Inheritance

class Teacher:

    def manage(self):
        print("Teaching Students.")


class Admin:

    def manage(self):
      print("Managing School.")


class Headmaster(Admin , Teacher):

    def guide(self):
        print("Guiding Teachers and Students")
        Teacher.manage(self)
        Admin.manage(self)

h1 = Headmaster()

h1.guide()


#3. Multilevel Inheritance

class Grandparent:

    def role(self):
      print("Grandparent gives values.")


class Parent(Grandparent):

    def responsibility(self):
      print("Parent take care of family.")


class Child(Parent):

    def study(self):
      print("child is studying......")


c1 = Child()

c1.role()
c1.responsibility()
c1.study()


#4. Hierarachical Inheritance

class Animal:

    def eat(self):
      print("Animal is Eating....")


class Dog(Animal):

    def sound(self):
      print("bhow....bhow....")


class Cat(Animal):

    def sound(self):
      print("Meow.....Meow......")


d = Dog()

d.eat()
d.sound()

c = Cat()

c.eat()
c.sound()


#5. Hybrid Inheritance

class Person:

    def work(self):
      print("Person is working....")


class Teacher(Person):

    def work(self):
      super().work()
      print("Teaching Students")


class Admin(Person):

    def work(self):
      super().work()
      print("Manage School.")


class Headmaster(Teacher , Admin):

    def work(self):
      super().work()
      print("Manage Teacher and Students")


h = Headmaster()

h.work()
             
      
    





















    





        
        
    
    
