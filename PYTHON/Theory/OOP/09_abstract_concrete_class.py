"""
Concrete & Abstract Class
Concrete Class: These are classes that are used to instantiate objects.
Abstract Class: These are classes that are not used to instantiate objects, they serve for inheritance
"""
from abc import ABC, abstractmethod

# Abstract Class
# SUPERCLASS = Abstract Class
# For a class became a real abstract class, she needs just one method with @abstractmethod
class Person(ABC): # ABC: Indicate a Abstract Class

    def __init__(self, name = None, birth_year = None, cpf = None, rg = None):
        self.name = name
        self.birth_year = birth_year
        self.cpf = cpf
        self.rg = rg
        print("Inside Person Class")
    
    
    def print_name(self):
        return self.name
    
    @abstractmethod # Indicate a Abstract Class
    def work(self):
        print("Working...")

# Concrete Class
# When a Concrete Class inherit a Abstract Class, she needs only one method to work otherwise it doesn't work
class Administrator(Person):
    
    def work(self):
        print("Analyzing Spreadsheets...")

# Concrete Class
class Teacher(Person):
    
    def work(self):
        print("Teaching...")

# Concrete Class
class Student(Person):
    pass

administrator_one = Administrator()
teacher_one = Teacher()
administrator_one.work()
teacher_one.work()