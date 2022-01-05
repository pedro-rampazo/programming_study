"""
Function Named Parameters
- To pass parameters without sequence
- Just indicate value with intern variables
"""


def register_function(intern_name, intern_last_name):
    print(f"Your name is: {intern_name} {intern_last_name}")

extern_name = input("Insert your name: ")
extern_last_name = input("Insert your last name: ")
register_function(intern_last_name = extern_last_name, intern_name = extern_name)