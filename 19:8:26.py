# raise Keyword

# Menually raises an exception

# raise ExceptionType("a clear message for explnaning what went wrong.")

# assert

# Checks weather a condition is True.

# assert condition , "message shown if the condition is False."

# Custom Exception

# User-defined exception created by inheriting from Exeption.

# raise keyword



age = 20  # ahi 20 ni jagya ee 18 karata nichheni age lakhavi ne to error ave but 18 karata uper lakhavi to error no ave 

if age < 18:
    raise ValueError("Age must be 18 or above.")






def get_age(age):
    if age < 0:
        raise ValueError("Age cannot be nagative.")
    return age

try:
    print(get_age(5))   # ahi 5 ni jagya ee jo minus value lakhava ma ave to error ave 
except ValueError as e:
    print(f"Error: {e}")





marks = 75

assert marks >= 0, "marks cannot be nagative."


def calculate_average(numbers):
    assert len(numbers) > 0 , "list cannot be empty"
    return sum(numbers) / len(numbers)

print(calculate_average([10 , 20 , 30]))





# Custom Exception


class InsufficientFundError(Exception):
    """Raised When a withdrawal excced the available balance."""
    pass

class BankAccount:

    def __init__(self , balance = 0):
        self.balance = balance


    def withdraw(self , amount):
        assert amount > 0 , "Withdrawal amount must be positive."
        if amount > self.balance:
            raise InsufficientFundError(f"cannot withdraw {amount} balance is only {self.balance}")
        self.balance -= amount
        return self.balance

account = BankAccount(1000)

try:
    account.withdraw(1000)
    account.withdraw(500)
except InsufficientFundError as e:
    print(f"Transaction failed: {e}")



































    





