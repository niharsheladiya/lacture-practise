age=20
if age>=18:
    print("you are eligible for vote")
    print("=====if else statements=====")
    

number=-5
if number>=0:
    print("positive number")
else:
    print ("negative number")
    print("======if elif else statements======")

    
    marks=82
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
else:
    print("Fail")
    print("=====match case======")


num1 = 10
num2 = 5
operator = input("Enter your operator sigh:")

match operator:
  case "+":
    print("Addtion:",num1+num2)
  case "-":
    print("Subtraction:",num1-num2)
  case "*":
    print("Multiplication:",num1*num2)
  case "/":
    print("division:",num1/num2)
  case _:
     print("Invalid operator") 
    
    
     
