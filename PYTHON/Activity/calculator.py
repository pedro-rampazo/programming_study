import math_operations_module

options = 0

while options not in range(1, 9):
    options = int(input("[1] % \n [2] 1/X \n [3] X² \n [4] √X \n [5] / \n [6] * \n [7] - \n [8] + \n \
Choose the operation: "))

first_value = int(input("Insert a value: "))

if options == 1:
    print(f"Result: {math_operations_module.per_cent(first_value)}")
elif options == 2:
    print(f"Result: {math_operations_module.one_sob_val(first_value)}")
elif options == 3:
    print(f"Result: {math_operations_module.val_squared(first_value)}")
elif options == 4:
    print(f"Result: {math_operations_module.square_root(first_value)}")
elif options == 5:
    print(f"Result: {math_operations_module.division(first_value)}")
elif options == 6:
    print(f"Result: {math_operations_module.multiplication(first_value)}")
elif options == 7:
    print(f"Result: {math_operations_module.subtraction(first_value)}")
else:
    print(f"Result: {math_operations_module.addition(first_value)}")