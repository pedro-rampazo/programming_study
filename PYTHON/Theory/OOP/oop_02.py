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
        self.account_number = account_number
        self.titular = titular
        self.balance = balance
    
    
    def extract(self):
        self.balance -= AccountBank.tax # Clear reference to class
        print(f"Your extract: {self.balance}")
    
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw_money(self, value):
        self.balance -= value

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