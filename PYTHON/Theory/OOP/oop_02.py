"""
Visibility - Access Modifier
→ Private (Restrictive) - Attributes and Methods can only be manipulated within the Class
→ Protected (Intermidiate) - Attributes and Methods can only be manipulated within Class and Subclass
→ Public (Les restrictive) - Attributes and Methods can be manipulated in anywhere in the code 
"""
class AccountBank:
    
    # Class Attribute → For fix attributes
    tax = 0.50

    # Class Method
    @classmethod
    def returnCode(cls):
        print("Código: 555")

    @staticmethod
    def returnBankCode():
        print("345")

    # Instance Attribute
    def __init__(self, account_number, titular, balance = 2000): # Balance with a default value
        self._account_number = account_number # Protected Visibility
        self.titular = titular # Public Visibility
        self.__balance = balance # Private Visibility
        
    
    def extract(self):
        self.__balance -= AccountBank.tax # Clear reference to class
        print(f"Your extract: {self.__balance}")
    
    
    def deposit(self, amount):
        self.__balance += amount
    
    
    def withdraw_money(self, value):
        self.__balance -= value

account_one = AccountBank(12345, "Pedro Rampazo")
account_two = AccountBank(54321, "João da Silva", 5000)

print(f"Account Number: {account_one.account_number} | Titular: {account_one.titular} | Balance: {account_one.balance}")
print(f"Account Number: {account_two.account_number} | Titular: {account_two.titular} | Balance: {account_two.balance}")

print(account_one.__dict__)
print(account_two.__dict__)

# Calling Class Method
AccountBank.returnCode()

# Calling Static Method
AccountBank.returnBankCode()