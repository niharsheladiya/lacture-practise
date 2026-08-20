# Python File Handling

# text file handling

# open() function

# file = open("fileNAME.txt" , "mode")

'''
Mode     meaning
r         read
w         write      
a         append
x     create new file
r+       read+write
w+       write+read
a+      append+read
r-          read
'''


files = open("demo.txt" , "w")

files.write("nihar\n")
files.write("Python\n")
files.write("Red and White\n")

files = open("demo.txt" , "r")

data = files.read()

print(data)

files.close()

file = open("demo.txt" , "a")

file.write("Javascript")

file = open("demo.txt" , "r")

data = file.read()

print(data)

file.close()

file = open("demo.txt" , "r")


print(file.readline())
print(file.readline())

print(file.readlines())


file = open("student.txt" , "x")

file.close()
