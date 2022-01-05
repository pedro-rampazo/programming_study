"""
Function Parameters
- To pass extern values in functions
- To execute a function you must pass the same parameters number
"""

def register_function(intern_name, intern_last_name):
    print(f"Your name is: {intern_name} {intern_last_name}")

extern_name = input("Type your name: ")
extern_last_name = input("Type your last name: ")
register_function(extern_name, extern_last_name)