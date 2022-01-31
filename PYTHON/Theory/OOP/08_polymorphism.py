"""
Polymorphism:
Overwritten concept in methods of th class
"""
class Person: 

    def __init__(self, name = None, birth_year = None, cpf = None, rg = None):
        self.name = name
        self.birth_year = birth_year
        self.cpf = cpf
        self.rg = rg
    

    def print_name(self):
        return self.name

    # work method that all Person subclasses inherit by default
    def work(self):
        print("Working...")

class Administrator(Person):
    # method overwrite
    def work(self):
        return "Analyzing spreadsheets...."

class Teacher(Person):

    def __init__(self):
        self.subjects = None

    # method overwrite
    def work(self):
        return "Teaching..."

class Student(Person):
    
    def __init__(self, name, birth_year, cpf, rg):
        super().__init__(name, birth_year, cpf, rg)
        self.enrollment = None
        self.grades = None
    
    def study(self):
        return "Studying..."

administrator_one = Administrator()
teacher_one = Teacher()
print(administrator_one.work())
print(teacher_one.work())