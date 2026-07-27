print("==========while loop==========")
i=1
while i<=5:
    print(i)
    i+=1
   
j=5
while j>=1:
    print(j)
    j-=1
    
    
print("=========for loop==========")
for i in range(1,6):
    print(i)

print("==========loop through strings==========")
name="python"
for j in name:
    print(j)


print("========loop through list==========")
fruits=["Apple","Banana","Orange","Mango"]
for item in fruits:
    print(item)



print("=======range(start,stop,step) function============")
for i in range (5):
    print(i)


    
print("==============") 
for i in range (1,6):
    print(i)

    
print("==============")
for i in range(0,10,2):
    print(i)
    


print("==============")  
for i in range(10,0,-1):
    print(i)



print("==============")
#nested loop in python
#a loop in another loop

for i in range(1,5):
 for j in range(1,9):
        print(j,end="")   #cheli 2 line ni badle print(j) pan chale
        print()    
    
print("========break statements===========")
#stop the loop immediately
for i in range(1,7):
    if i==4:
        break
    print(i)


print("==========continue statements============")
#skips current iteration
for i in range(1,7):
    if i==5:
        continue
    print(i)



print("=============pass statements=============")
#it will pass the iteration as our car pass through toll plaza
for i in range(1,7):
    if i==4:
        pass
    print(i)

    


    
