"""
ENCAPSULATION:
Combine two or more methods into one
"""
class AccountBank:

    tax = 0.50
    
    def __init__(self, account_number, titular, balance = 2000):
        self._account_number = account_number
        self.titular = titular
        self.__balance = balance
    

    def extract(self):
        self.__balance -= AccountBank.tax
        print(f"Your extract: {self.__balance}")
    

    def deposit(self, amount):
        self.__balance += amount
    

    def withdraw(self, value):
        self.__balance -= value
    
    # Encapsulation Method
    def transfer(self, value, destination):
        self.withdraw(value)
        destination.deposit(value)

account_one = AccountBank(123, "Mona Lisa", 2300)
account_two = AccountBank(345, "Albert")

account_one.transfer(300, account_two)
account_one.extract()
account_two.extract()
