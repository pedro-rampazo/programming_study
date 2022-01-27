"""
Visibility - Access Modifier
→ Private (Restrictive) - Attributes and Methods can only be manipulated within the Class
→ Protected (Intermidiate) - Attributes and Methods can only be manipulated within Class and Subclass
→ Public (Less restrictive) - Attributes and Methods can be manipulated in anywhere in the code 
"""
class AccountBank:

    tax = 0.50
    
    def __init__(self, account_number, titular, balance = 2000):
        self._account_number = account_number # Protectd Visibility
        self.titular = titular # Public Visibility
        self.__balance = balance # Private Visibility
    
    def extract(self):
        self.__balance -= AccountBank.tax
        print(f"Your extract: {self.__balance}")
    

    def deposit(self, amount):
        self.__balance += amount
    

    def withdraw(self, value):
        self.__balance -= value

account_one = AccountBank(345, "Pedro", 5000)
account_one.extract() # The only way to view balance