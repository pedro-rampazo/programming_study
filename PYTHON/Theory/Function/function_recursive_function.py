"""
Recursive Function
- Almost used a Loop effect with the own function
"""

def reduce_number(intern_number):
    print(intern_number)
    if intern_number > 0:
        intern_number -= 1
        reduce_number(intern_number)

reduce_number(5)