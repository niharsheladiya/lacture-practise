# math and random module in python

import math
import random


number = int(input("Enter a number:"))

print("Square root:" , math.sqrt(number))
print("Power , 2:" , math.pow(number , 2))
print("Factorial:" , math.factorial(number))



radius = float(input("Enter radius of the circle:"))

area = math.pi * radius * radius

print("Circle Area:" , area)



num = float(input("Enter a number for natural Logarithm:"))

if num > 0:
    print(math.log(num))
else:
    print("Natural Logarithm is possible only for positive number.")



# Trigonometry


angle = float(input("Enter a angle in degree:"))

angle_radian = math.pi / 180 * angle

print("sin" , math.sin(angle_radian))
print("cos" , math.cos(angle_radian))



# ceiling , floor and Absolute


value = float(input("Enter a decimal number:"))

print("value:" , value)
print("Ceiling value:" , math.ceil(value))
print("Floor value:" , math.floor(value))
print("Absolute value:" , math.fabs(value))


# Random number


numbers = []

for i in range(10):
    number = random.randint(1 , 10)
    numbers.append(number)

print(numbers)



# dice and shuffle


dice = random.randint(0 , 1)
print("Dice Rolled:" , dice)

players = ["Rohit" , "Sachin" , "Rahul" , "Virat" , "Samson"]

print(players)

random.shuffle(players)

print("Shuffle Players:" , players)

students = ["Rahul" , "Vivek" , "Pal" , "Nikunj" , "Vrutika"]

student = random.choice(students)

print(student)



# UUID : UUID1 , UUID2 , UUID3 , UUID4 , UUID5

# 1. UUID1 - Time Based

import uuid


id = uuid.uuid1()

print(id)


# UUID2 - DCE Security

# Python UUID2 is based on DCE Security must be focus on security parameters.

# Python standard uuid does not provide a direct uuid2() function.


id = uuid.uuid3(
    uuid.NAMESPACE_DNS,
    "redandwhite.com"
)

print(id)

#UUID$

# Real-world

# E-commerce + order_id
# College + student_id
# Banking + Transaction id
# API + Request ID
# Database + Record ID

id = uuid.uuid4()

print(id)



students = {
    "ST001" :uuid.uuid4(),
    "ST002" :uuid.uuid4(),
    "ST003" :uuid.uuid4(),
    "St004" :uuid.uuid4()
}

print("StudentID and UUID")

for student_id , student_uuid in students.items():
    print(student_id , ":" , student_uuid)

uuid1 = uuid.uuid4()
uuid2 = uuid.uuid4()

if uuid1 == uuid2:
    print("Both uuid are equal")
else:
    print("Both UUID are diffrent")

orders = []

for i in range(3):
    order_id = uuid.uuid4()
    orders.append(order_id)

print("E-commerce Order ID:")

for order in orders:
    print(order)

student_data = [
    {"name":"Rahul" , "age":22},
    {"name":"Rajesh" , "age":85},
    {"name":"Priya" , "age":24},
    {"name":"Amit" , "age":28}
]

sorted_students = sorted(student_data , key=lambda student:student["age"])
# ahi chele age ni jagya ee name lakhata name prama ne data sort kare che

for student in sorted_students:
    print(student)




