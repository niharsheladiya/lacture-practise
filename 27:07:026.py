#minimum and maximum value find Element....

rows=int(input("rows:"))
clos=int(input("clos:"))

matrix=[]

for i in range(rows):
    row=list(map(int,input(f"Enter row {i+1}:").split()))
    matrix.append(row)

max_value = matrix[0][0]
min_value = matrix[0][0]


for row in matrix:

    for value in row:

        if value > max_value:

            max_value = value

        if value < min_value:

            min_value = value



print("Max-value : ",max_value)
print("Min-value : ",min_value)



#Sorting in Integer list

number = list(map(int , input(f"Enter Numbers:").split()))

number.sort()

number.sort(reverse=True) #ahi jo true ni jagya e flase hoy to incresing order ma ave or jo aa line ne (#) lagadta commet thay to pan incrseing order ma ave baki reverse order ma decresing order male 

print(number)


#Sort List of tuples by second Element

students = [
    ("ved",80),
    ("pal",90),
    ("vatsal",30),
    ("dixit",70)
]

sorted_student = sorted(students,key = lambda x : x[1])

print(sorted_student)


#sort dictionary list by key

employee = [
    {"name" : "raj","salary":30000},
    {"name" : "shrey","salary":5000000},
    {"name" : "pal","salary":100000000},
    {"name" : "vatsal","salary":1},
    {"name" : "ved","salary":600000},
]

result = sorted(employee,key = lambda x : x["salary"])


print(result)


































