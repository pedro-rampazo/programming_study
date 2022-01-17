"""
Object-Oriented Paradigm (OOP)

Class:
    → Object
    → Construct
    → Attribute
    → Method

EXAMPLE
Class:              Aeroplane
Object:             Boeing 347 type Aeroplane
Attribute:          Wings, Turbines and Landing Gear...
Method:             Fly(), Land() and TakeOff()...
Construct:          An implicity created function with the same name as the class
"""
class Patient:

    def __init__(self, name, age, cpf, email):
        print("Allowed Access!")
        self.name = name
        self.age = age
        self.cpf = cpf
        self.email = email
