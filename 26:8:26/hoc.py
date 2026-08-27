# map function

names = ["rahul" , "amit" , "priya" , "vivek"]

# uppercase_names = list(map(str.capitalize , names))

upper_case = [name[0].upper() + name[1:-1] + name[-1].upper() for name in names]

print(upper_case)


numbers = [1 , 2 , 3 , 4 , 5]

result = list(map(lambda x : x * 2 , numbers))

print(result)

# reduce(Func , initialValue)

from functools import reduce

numbers = [10 , 20 , 30 , 40 , 50 , 50]

result = reduce(lambda x , y:x * y , numbers)

print(result)

# largest word

words = ["Python" , "Java" , "Javascript" , "HTML" , "Programming"]

long_word = reduce(lambda x , y : x if len(x) > len(y) else y , words)

print(long_word)


numbers = [10 , 15 , 20 , 25 , 30 , 35 , 40 , 45]

even_num = list(filter(lambda x : x % 2 != 0 , numbers))

print(even_num)
