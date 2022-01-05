"""
This module have many basic math operations
There are:
- per cent          (%)
- one sob val       (1/X)
- value squared     (X²)
- square root       (√X)
- division          (X:Y)
- multiplication    (X*Y)
- subtraction       (X-Y)
- addition          (X+Y)
"""
from math import sqrt

def another_value():
    """
    another_value() function:
    For math operations with one more value
    """
    return int(input("Insert another value: "))


def per_cent(intern_value):
    """
    per_cent() function:
    Calculate value in per cent
    """
    return intern_value / 100


def one_sob_val(intern_value):
    """
    one_sob_val() function:
    1 / X 
    """
    return intern_value ** -1


def val_squared(intern_value):
    """
    val_squared() function:
    A value with 2 elevate
    """
    return intern_value ** 2


def square_root(intern_value):
    """
    square_root() function:
    A square root of a value
    """
    return sqrt(intern_value)


def division(intern_value):
    """
    division() function:
    A division between two values
    """
    second_value = another_value()
    return intern_value / second_value


def multiplication(intern_value):
    """
    multiplication() function:
    A multiplication between two values
    """
    second_value = another_value()
    return intern_value * second_value


def subtraction(intern_value):
    """
    subtraction() function:
    A subtraction between two values
    """
    second_value = another_value()
    return intern_value - second_value


def addition(intern_value):
    """
    addition() function:
    A addition between two values
    """
    second_value = another_value()
    return intern_value + second_value