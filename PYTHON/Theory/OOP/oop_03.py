from datetime import date

class Patient:

    def __init__(self, name, age, cpf, email):
        self.name = name
        self.age = age
        self.cpf = cpf
        self.email = email
    
    
    @classmethod
    def ageBirthYear(cls, name, birthYear, cpf, email):
        age = date.today().year - birthYear
        return cls(name, age, cpf, email)

patient = Patient("Pedro Rampazo", 21, "000.000.000-00", "pedro.rampazo@hotmail.com")
print(patient.__dict__)
print(Patient.ageBirthYear(2000))

patient = Patient.ageBirthYear("Pedro Rampazo", 2000, "000.000.000-00", "pedro.rampazo@hotmail.com")
print(patient.__dict__)
print(patient.age)
