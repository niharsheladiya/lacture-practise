#sets,dictionary,type conversion,list of dictionary

#Q-1:
print("="*40)
print("1. sets operation")
print("="*40)

numbers={1,2,3,4,5}
numbers.add(6)
numbers.remove(3)
print("is 2 present?",2 in numbers)
print(numbers)
print(type(numbers))





#Q-2:
print("="*40)
print("2.union,intersection,difference")
print("="*40)

set_a={1,2,3,4}
set_b={3,4,5,6}

print(set_a)
print(set_b)

print("Union:",set_a.union(set_b))
print("Intersection:",set_a.intersection(set_b))
print("Difference:",set_a.difference(set_b))
print("Difference:",set_b.difference(set_a))



                      

#Q-3:
print("="*40)
print("3.Dictionary operation")
print("="*40)           


student={
    "name":"rahul",
    "age":"20",
    "grade":"a" 
    }

for key in student.keys():
    print(key)
for value in student.values():
    print(value)


print(student['name'])
student["city"]="delhi"
student["age"]="21"
print(student)
del student["grade"]
print(student)




#Q-4:
print("="*40)
print("4.Dictionary from two lists")
print("="*40)


keys=['id','name','email']
values=['101','rajan','rajan@gmail.com']


user={}
for i in range(len(keys)):
    user[keys[i]]=values[i]
    print(user)


#Q-5:
print("="*40)
print("5.convert")
print("="*40)
   
num='123'
print(type(num))
nums=int(num)
print(type(nums))
list=[1,2,3,4]
tuple=tuple(list-1)
print(tuple-1)
pairs=[(1,"A"),(2,"B")]








 

































