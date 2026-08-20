# Python Function

# Built-in Functions

print("="*20)
print("Functions with Python")
print("="*20)

numbers = [1 , 45 , 85 , 22 , 66 , 34]

print(numbers)

print(len(numbers))

print(max(numbers))

print(min(numbers))

print(sorted(numbers))

print(sum(numbers))


print("="*20)
print("UDF Functions")
print("="*20)


def add(a , b):
    print(a + b)


add(10 , 20)
add(20 , 20)


'''
1. Reusability
2. Cleaner Code
3. Better Organization
4. Reduce repetition
'''


print("="*20)
print("Recursion")
print("="*20)

# A function calling itself.

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(10))

# Sum of numbers


def total(n):

    if n == 0:
        return 0

    return n + total(n - 2)


print(total(10))


# Anonymous Function / Lambda Functions

square = lambda x : x * x

print(square(5))



add = lambda a , b : a + b

print(add(10 , 20))
    

















































