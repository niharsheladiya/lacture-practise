
file = open('notes.txt' , 'wSupport')

file.close()



file = open('notes.txt' , 'a')

file.write("Line 4: Python Support multiple of file handeling.")

file.close()

print("Data added.")

file = open('notes.txt' , 'rb')

data = file.read()

print(data)

file.close()




file = open('notes.txt' , "r")

data = file.read()

result = data.splitlines()

print(result)
print("Words:" , len(data.split()))
print("Characters:" , len(data))
print("Lines:" , len(data.splitlines()))




file = open("notes.txt" , "r+")

print(file.read())

file.write("\nthis is append line.")

file.close()




word = input("Enter word:")
file = open("notes.txt" , "r")

line_no = 1

for line in file:
    if word in line:
        print("Word found at line:" , line_no)
    line_no += 1
file.close()




file1 = open("notes.txt" , "r")

data = file1.read()

file1.close()

file2 = open("newFile.txt" , "x")

file2.close()

file2 = open("newFile.txt" , "w")

file2.write(data)

file2.close()

print("File copied.....")


