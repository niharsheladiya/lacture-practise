# Global Keyword in Python


total = 0


def increment():
    global total
    total += 2


increment()
increment()
increment()
print(total)


# Multiple return Values


def calculation(a , b , c):

    total = a + b + c

    average = total / 3

    maximum = max(a , b , c)

    minimum = min(a , b , c)

    return total , average , maximum , minimum

total , average , maximum , minimum = calculation(10 , 20 , 30)

print(total)



# Lambda with reduce()

from functools import reduce

numbers = [1 , 2 , 3 , 4 , 5]

product = reduce(lambda x , y : x * y , numbers)

print(product)



# Global vs Local Variables

name = "python"

def demo():
    global name
    name = "javascript"

    print(name)

demo()
print(name)




# return multiple values (student result)

def result(m1 , m2 , m3):

    total = m1 + m2 + m3

    percentage = total / 3

    if percentage >= 90:

        grade = "A"

    elif percentage >= 75:

        grade = "B"

    elif percentage >= 60:

        grade = "C"

    else:

        grade = "Fail"

    return total , percentage , grade

total , percentage , grade = result(90 , 89 , 95)

print(total)
print(percentage)
print(grade)
    













