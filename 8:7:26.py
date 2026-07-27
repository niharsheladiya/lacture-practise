#basic pattern in python


#1. pattern (without space)
size=5
for i in range(size):
    for j in range(size):
        print("*",end="")
    print()


#2.right angled triangle pattern
size=int(input("Enter your size:"))
for i in range(1,size+1):
    for j in range(i):
        print("*",end="")
    print()

#3.inverted right angled triangle pattern
size=5
for i in range(size,0,-1):
    for j in range(i):
        print("*",end="")
    print()

#4.pattern (with space)
#pyramid patterns

rows=5

for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

#inverted pyramid

rows=5
for i in range(4,0,-1):      #ahi je 4 lakhyo che karan ke 9* vali line 2 times apti teni badle 1 time ave
    for j in range(rows-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

#Diamond Ptterns
rows=5

for i in range(1,rows+1):
    print(" "*(rows-i),end="")

    if i==1:
        print("*")
    #elif i==rows:
        #print("*"+" "*(2*rows-i))
    else:
        print("*"+" "*(2*i-3)+"*")  
    


for i in range(rows-1,0,-1):
    print(" "*(rows-i),end="")

    if i==1:
        print("*")
    else:
        print("*"+" "*(2*i-3)+"*")
    













        
    
    
        
    
