#polymorphism

#Polymorphism mean 'one name , many forms.'

#Overloading Method

#Overriding Method

#Method Overloading mean having multiple method with the same name but diffrent parameter.



class Calculator:

    def add(self , a , b=0 , c=0):
        return a + b + c

c = Calculator()

print(c.add(10 , 20))
print(c.add(10 , 20 , 30))



#*args

class Calculator:

    def add(self , *number):
        return sum(number)


c1 = Calculator()

print(c1.add(10 , 20))
print(c1.add(10 , 20 , 30))
print(c1.add(10 , 20 , 30 , 40))


#Overriding Method

#Method of overriding occurs when a child class provides its own implementation of a method already defined in the parent class.


class Animal:

    def sound(self):
        print("Animal make sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        #Animal.sound(self)  #aano use karvo hoy too super vala ne comment karvo pade and jo super vaparvo hoy to Animal ne comment karvi pade
        print("BHow... Bhow...")

d = Dog()
d.sound()


class Employee:

    def work(self):
        print("Employee is working")


class Developer:

    def work(self):
        print("Developer is working on Developer")


class Designer:

    def work(self):
        print("Designer is working on Design")
        
employee = [Employee() , Developer() , Designer()]


for employ in employee:
    employ.work()


#issubclass()
#issubclass(childclass , parentclass)

class Employee:

    def work(self):
        print("Employee is working.")


class Developer(Employee):

    def work(self):
        print("Developer is working on code")


class Designer(Developer):

    def work(self):
        print("Designer is working on design")


employee = [Employee() , Developer() , Designer()]


for employ in employee:
    employ.work()


print(issubclass(Developer , Employee))
print(issubclass(Designer , Employee))
print(issubclass(Designer , Developer))

# Child inherits from both parent and mother

# super()

# super() is used to access parent class methods or constructor from the child class.



            





        
             

    














    
