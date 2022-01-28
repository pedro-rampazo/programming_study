# Create a class that has some attributes used by other classes
from unicodedata import name

# SUPERCLASS is when a class is used in multiple times
class Person: 

    # This class have attributes that can be used by Student() and Teacher()
    def __init__(self, name, birth_year, cpf, rg):
        self.name = name
        self.birth_year = birth_year
        self.cpf = cpf
        self.rg = rg
    

    def print_name(self):
        return self.name

# SUBCLASS is when a class is used in specific situations
# The classes must only have specific attributes
class Student(Person):
    
    def __init__(self, name, birth_year, cpf, rg):
        # Use super() for SUPERCLASS
        # With super() don't need of the self parameter
        super().__init__(name, birth_year, cpf, rg) #Now you can call attributes and method within Student class
        self.enrollment = None
        self.grades = None
    
    def study(self):
        return "Studying..."
    
class Teacher:

    def __init__(self):
        self.subjects = None


    def teach(self):
        return "Teaching..."

student_one = Student("Sérgio", 1990, "123.456.789-00", "23.456.789-X")
print(student_one.print_name())
