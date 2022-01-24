"""
- Default parameters is indicate to use not obligatory
- Is not necessary pass parameters for default parameters
"""


def register_function(intern_name, intern_last_name, intern_age = None):
    print(f"Name: {intern_name} | Last Name: {intern_last_name} | Age: {intern_age}")

extern_name = input("Insert your name: ")
extern_last_name = input("Insert your last name: ")
extern_age = int(input("Insert your age: "))
register_function(extern_name, extern_last_name) # Is not necessary to pass default parameter