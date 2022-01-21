"""
OBJECT PROPERTIES:
- Attributes: They are declared in the __init__() function
- Methods
→ THE BEST WAY TO DIFFERENTIATE OBJECT AND CLASS PROPERTIES IS TO USE OBJECT ATTRIBUTES!!!!
"""
class AccountBank:

    def __init__(self, account_number, titular, balance = 2000): # Balance parameter have a default value
        # Object attributes
        self.account_number = account_number
        self.titular = titular
        self.balance = balance

    # Method of the object
    def extract(self):
        print(f"Your extract: {self.balance}")


    def deposit(self, amount):
        self.balance += amount
    

    def withdraw(self, value):
        self.balance -= value

# Instantiating the object
account_one = AccountBank(123, "Pedro Rampazo", 10000)

# Calling attributes of the object
print(f"Account Number: {account_one.account_number}")
print(f"Titular: {account_one.titular}")
print(f"Balance: {account_one.balance}")

# Calling methods of the object
account_one.extract()

# Calling method of the object with parameters
account_one.deposit(200)
account_one.withdraw(500)
account_one.extract()
