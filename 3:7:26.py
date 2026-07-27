# Python Collection
print("====== Python Collection =======")

# List
list1 = [10, 20, 30, 40]

print(type(list1))
print(list1)

print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])

for i in list1:
    print(i)

# Mutability
list1[1] = 200
print("After modification:", list1)

    
#append()

list1.append(50)
list1.append(60)

print(list1)

#operation

print("Max:",max(list1))
print("Min:",min(list1))

list1.append(10)

print(list1)


#remove duplicate value

unique = []

for i in list1:
    if i not in unique:
        unique.append(i)

print(unique)        


#tuple

tuple1=(1,2,3,4,4,2,2,3)

print(tuple1[0])



#count

print("count of 2:",tuple1.count(4))


#swipping using tuple

a,b=10,20

print(a)
    
a,b=b,a

print(a)
print(a,b)


#set

data = [1,2,3,4,5,6,6]

set1 = set(data)

print(set1)


#set operation

a={1,2,3}
b={4,5,6,1}

print(a|b)

print(a&b)


set1.add(10)
set1.remove(1)


print(set1)


#dictionary

dict1={
    "name":"Rahul",
    "Age":"18"
    }

print(dict1["name"])
print(dict1.get("Age"))


dict1["name"] = "Nihar"

print(dict1)




































































