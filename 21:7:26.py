# Create a 1D arret (list) with five integer elements. Display the arrey using a loop.

arr = []


for i in range(5):
    num = int(input(f"Enter Element {i + 1}:"))
    arr.append(num)

print("Arrey Element")

for i in arr:
    print(i)
print()
print(arr)


# develop a program to calculate the sum of all elements in a 1D arrey separately.


total = 0;

for i in arr:
    total += i

print("Total:" , total)


# create a program to insert a new element at a specific position in a 1D arrey.

position = int(input("Enter Position (0 - 4):"))

value = int(input("Enetr new Element:"))

arr.insert(position , value)

print(arr)


# Write a program to delete an element by its value from a 1D arrey

value = int(input("Enter element to delete:"))

if value in arr:
    arr.remove(value)
    print(arr)
else:
    print("Element not found.")


# Develop a program to update an element in a 1D arrey based on its index

index = int(input("Enter index to update:"))
new_value = int((input("Enter new value:")))


if 0 <= index < len(arr):
    arr[index] = new_value
    print(arr)
else:
    print("Invalid Index")


# Implement a program to search for an element in a 1D arrey and return its index.


key = int(input("Enter Element to search:"))

if key in arr:
    print(arr.index(key))
else:
    print("Enter not found")
                  


    
          
                    
