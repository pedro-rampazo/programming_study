"""
Activity function #03
- Read first_value variable
- Insert options: [1] % | [2] 1/X | [3] x² | [4] √X | [5] / | [6] * | [7] - | [8] +
- Call function for each situation
- 5, 6, 7, 8 selection read one more number
- print result
"""
import math

first_value = int(input("Insert a value: "))
options = 0


def another_value():
    return int(input("Insert another value: "))


def per_cent(intern_value):
    return intern_value / 100


def one_sob_val(intern_value):
    return intern_value ** -1


def val_squared(intern_value):
    return intern_value ** 2


def square_root(intern_value):
    return math.sqrt(intern_value)


def division(intern_value):
    second_value = another_value()
    return intern_value / second_value


def multiplication(intern_value):
    second_value = another_value()
    return intern_value * second_value


def subtraction(intern_value):
    second_value = another_value()
    return intern_value - second_value


def addition(intern_value):
    second_value = another_value()
    return intern_value + second_value



while options not in range(1, 9):
    options = int(input("[1] % \n [2] 1/X \n [3] X² \n [4] √X \n [5] / \n [6] * \n [7] - \n [8] + \n \
Choose the operation: "))

if options == 1:
    print(f"Result: {per_cent(first_value)}")
elif options == 2:
    print(f"Result: {one_sob_val(first_value)}")
elif options == 3:
    print(f"Result: {val_squared(first_value)}")
elif options == 4:
    print(f"Result: {square_root(first_value)}")
elif options == 5:
    print(f"Result: {division(first_value)}")
elif options == 6:
    print(f"Result: {multiplication(first_value)}")
elif options == 7:
    print(f"Result: {subtraction(first_value)}")
else:
    print(f"Result: {addition(first_value)}")