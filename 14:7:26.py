# Student Mangement System

print("="*40)
print("Student Mangement System")
print("="*40)

number = [1 , 2 , 3 , 4 , 5]


students = [
    {"id":101 , "name":"Rahul" , "score":78},
    {"id":102 , "name":"Rajesh" , "score":65},
    {"id":103 , "name":"Ronak" , "score":55},
    {"id":104 , "name":"Rohan" , "score":87}
]


print(students[0]['name'])
print(students[1]['name'])
print(students[2]['name'])

print(students)

print("="*40)
print("Student Name List")
print("="*40)


for student in students:
    print(student["name"])


print("="*40)
print("Student Average Score")
print("="*40)


sum = 0


for student in students:
    sum += student['score']

average = sum / len(students)


print("\n Average Studnet Score:" , average)


print("="*40)
print("Add New Student")
print("="*40)


students.append({
    "id":105,
    "name":"Raj",
    "score":75
    })

print(students)


print("="*40)
print("Update Student Score")
print("="*40)


students[1]['score'] = 88


for student in students:
    if student['id'] == 102:
        student['score'] = 88

print(students)

print("="*40)
print("Remove Studnet From List")
print("="*40)


for student in students:
    if student['name'] == 'Ronak':
        students.remove(student)
        break;


print(students)


print("="*40)
print("Student Score > 80")
print("="*40)



for studnet in students:
    if studnet['score'] > 80:
        print(student['name'])


print("="*40)
print("Sort Decending")
print("="*40)
      



















































