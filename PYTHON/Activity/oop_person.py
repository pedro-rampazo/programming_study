"""
Crie uma classe para representar uma pessoa, com atributos privados de nome, idade e altura. Crie os métodos públicos
necessários para sets e gets e também um método para imprimir os dados da pessoa.
"""
class Person:

    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height
    
    
    def get_name(self):
        return self.__name
    

    def get_age(self):
        return self.__age
    

    def get_height(self):
        return self.__height
    
    
    def set_name(self, new_name):
        self.__name = new_name
    

    def set_age(self, new_age):
        self.__age = new_age
    

    def set_height(self, new_height):
        self.__height = new_height
    

    def print_name(self):
        print(self.get_name())
    

    def print_age(self):
        print(self.get_age())


    def print_height(self):
        print(self.get_height())

pedro = Person("Pedro", 41, 1.65)
pedro.print_height()
pedro.set_height(1.90)
pedro.print_height()
    
