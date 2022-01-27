"""
Getters And Setters:
For private and protected attributes, we can use getters and setters functions to use this values.
With "@property" and "@name_function.setter" we can call the functions like attributes
"""
class Student:

    def __init__(self, name, age, registration):
        self.__name = name
        self._age = age
        self.__registration = registration
        self.__grades = None
    
    # Using for Getters
    @property
    def name(self):
        return self.__name

    # Using for Setters
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        self._age = new_age



student_one = Student("Pedro", 15, 123456)

# Calling Getters like attributes
print(student_one.name)
# Calling Setters like attributes
student_one.name = "Ricardo"
print(student_one.name)
