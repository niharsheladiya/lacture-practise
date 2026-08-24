# Common Typecodes

'''
arreyIdentifierName = arrey(typecode , [initilizer])


"i" : "integer"
"f" : "float"
"d" : "double"
"u" : "Unicode Character"


Notes: Arrey cannot store heterogeneous data. if you need diffrent datatype together , use a list
'''


from array import *

myarray = array('i' , [1 , 2 , 3 , 4 , 5])

print(myarray)

for i in myarray:
    print(i)



# Using for loop = append()
# Ask the user how many element they want to enter.
# Create an empty list.
# Use a for loop to take input.
# Store each element using append()


size = int(input("Enter size of arrey:"))

numbers = []

for i in range(size):
    value = int(input(f"Enter Element {i + 1} : "))
    numbers.append(value)


print("Arrey Elements:")

prinr(numbers)











