#1. Multiple Objects with Destructor

class Customer:

    def __init__(self , name):
      self.name = name
      print(f"{self.name} logged in.")

    def shopping(self):
      print(f"{self.name} is shopping.")


    def __del__(self):
      print(f"{self.name} logged out.")


c1 = Customer("Ved")
c2 = Customer("Nidhi")
c3 = Customer("Nihar")

c1.shopping()
c2.shopping()
c3.shopping()

del c1
del c2
del c3


#Default Constructor,Destructor

class Employee:

    def __init__(self):
      self.name = "ved"
      self.department = "cse"
      print(self.name , "joined office.")

    def display(self):
      print("Employee:" , self.name)
      print("Department:" , self.department)

    def __del__(self):
      print(self.name , "Left Office.")

emp = Employee()

emp.display()

del emp


# Bank Account

class BankAccount:

    def __init__(self , account_holder , account_number , balance):
      self.account_holder = account_holder
      self.account_number = account_number
      self.__balance = balance  #__ mean private variable

    def deposit(self , amount):

      if amount > 0:
        self.__balance += amount
        print(f"${amount} Deposited Successfully!.")

      else:
          print("Invaild amount.")


    def withdraw(self , amount):

      if amount <= 0:
        print("Invaild amount.")

      elif amount > self.__balance:
        print("Insufficient amount.")

      else:
        self.__balance -= amount
        print(f"${amount} withdraw Successfully!.")

    def check_balance(self):
      print(f"Current Balance: ${self.__balance}")

    def display(self):

      print("====== Account Details ========")

      print("Account Holder:" , self.account_holder)
      print("Account Number:" , self.account_number)
      print("Account Balance:" , self.__balance)


name = input("Enter Account Holder Name:")
acc_num = int(input("Enter Account Number:"))
balance = float(input("Enter Opening amount:"))
account = BankAccount(name , acc_num , balance)


while True:

   print("1. Deposit")
   print("2. Withdraw")
   print("3. Check Balance")
   print("4. Display")
   print("5. Exit")

   choice = int(input("Enter your choice:"))


   if choice == 1:

      amount = float(input("Enter deposit amount:"))
      account.deposit(amount)
        
   elif choice == 2:

     amount = float(input("Enter withdraw amount:"))
     account.withdraw(amount)

   elif choice == 3:

     account.check_balance()

   elif choice == 4:

     account.display()

   elif choice == 5:

     print("Thank you!!!")
     break

   else:
       print("Invalid Choice")
        
        
        
                             

    
                 









































