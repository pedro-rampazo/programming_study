"""
Activity function #02:
- Read Base and Exponent variables
- Create potentiation function
- Print return potentiation()
"""
base = int(input("Insert the base of the potentiation: "))
exponent = int(input("Insert the exponent of the potentiation: "))


def potentiation(intern_base, intern_exponent):
    return intern_base ** intern_exponent

print(f"Result potentiation: {potentiation(base, exponent)}")