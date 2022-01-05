"""
*args Parameter
- *args is a Tuple
- Receive many parameters inside within it
"""


def register_function(intern_name, intern_last_name, *args):
    print(f"Name: {intern_name} | Last Name: {intern_last_name} | Others: {args}")

extern_name = input("Insert your name: ")
extern_last_name = input("Insert your last name: ")
extern_age = int(input("Insert your age: "))
extern_phone = input("Insert your fone: ")
register_function(extern_name, extern_last_name, extern_age, extern_phone)
