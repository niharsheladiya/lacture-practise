# Arbitrary Arguments (*args)

# Wrire a Python function that accept any number of arguments and return their sum.

def addition(*args):
    total = 0


    for i in args:
        total += 1

    return total

addition(10 , 20 , 30 , 40 , 50)




# Keyword Arguments (**kwargs)

# Write a Python function that accept student information using keyword arguments and prints all student details.


def student (**kwargs):
    print("Student Details")


    for key , value in kwargs.items():
        print(f"{key} : {value}")


student(name = "vivek" , age = 25 , city = "surat" , course = "Python")




# doc (Documentation String)

# Write a function to calculate the area of a rectangle and display its Documentation.


def rectangle(length , width):
    """

    Function Name : rectangle

    Purpose:
        Calculate rectangle area.

    Parameter:
        length : int
        width : int

    Return:
        Area of rectangle

    """
    return length * width

print("Area :" , rectangle(10 , 20))
print(rectangle.__doc__)




# Lambda with map()

numbers = [10 , 15 , 20 , 25 , 30 , 35]

result = list(map(lambda x : x ** 2 , numbers))

print(result)






# Lambda with filter()

numbers = [10 , 15 , 20 , 25 , 30 , 35]

even = list(filter(lambda x : x % 2 != 0 , numbers))

print(even)




# Lambda with sorted()


students = [("vivek" , 85) , ("Rajesh" , 72) , ("Amit" , 22) , ("Raj" , 50)]

print(students)

result = sorted(students , key = lambda x : x [1])

print(result)




































        


