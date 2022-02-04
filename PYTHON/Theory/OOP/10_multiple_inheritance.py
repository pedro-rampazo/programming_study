"""
Multiple Inheritance
A class can inherit more than one class

Example:
→ FrontEnd
→ BackEnd
→ FullStack = FrontEnd + BackEnd
"""
class Employee:
    def work(self):
        print("Employee working...")

class FronEnd(Employee):
    def work(self):
        print("FrontEnd working...")

class BackEnd(Employee):
    def work(self):
        print("BackEnd working...")

class FullStack(FronEnd, BackEnd): # with a polymorphism, he executes the first inheritance
    pass

employee_one = FullStack()
employee_one.fe_work()
employee_one.be_work()
employee_one.em_work()