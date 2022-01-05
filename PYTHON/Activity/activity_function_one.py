"""
Activity function #01:
- Read X and Y variables
- Create biggest_number function
- Create average function
- Print return biggest_number()
- Print return average()
"""
x = int(input("Insert first number: "))
y = int(input("Insert second number: "))


def biggest_number(internX, internY):
    if internX >= internY:
        return internX
    else:
        return internY


def average(internX, internY):
    return (internX + internY) / 2

print(f"The biggest number is: {biggest_number(x, y)}")
print(f"The average is: {average(x, y)}")