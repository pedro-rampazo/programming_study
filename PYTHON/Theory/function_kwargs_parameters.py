"""
**kwargs Parameter
- **kwargs is a dictionary
- Use this for pass a dictionary as parameter
"""

def register_function(kwargs):
    print(f"Name: {kwargs['name']} | Last Name: {kwargs['last_name']}")

personal_data = {'name': None, 'last_name': None}
name = input("Insert your name: ")
personal_data.update({'name': name})
last_name = input("Insert your last name: ")
personal_data.update({'last_name': last_name})
register_function(personal_data)
