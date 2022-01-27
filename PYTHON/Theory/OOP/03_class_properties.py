"""
CLASS PROPERTIES:
- Attributes
- Methods
→ THE BEST WAY TO DIFFERENTIATE OBJECT AND CLASS PROPERTIES IS TO USE OBJECT ATTRIBUTES!!!!
"""
class AccountBank:

    # Class Attribute → For fix attributes
    tax = 0.50

    #Class Method
    @classmethod
    # For @classmethod it is necessary to declare "cls"
    def returnCode(cls):
        print("Code: 555")

    # For @staticmethod it is not necessary to declare "cls"
    @staticmethod
    def returnBankCode():
        print("345")

    def __init__(self, account_number, titular, balance = 2000):
        self.account_number = account_number
        self.titular = titular
        self.balance = balance

    
    def extract(self):
        # For call a class attribute we use the class name
        self.balance -= AccountBank.tax
        print(f"Your extract: {self.balance}")


    def deposit(self, amount):
        self.balance += amount
    

    def withdraw(self, value):
        self.balance -= value

print(f"Bank tax: {AccountBank.tax}")
# Calling Class Method
AccountBank.returnCode()
AccountBank.returnBankCode()
account_one = AccountBank(123, "Pedro", 3500)
# Calling Object Method
account_one.extract()