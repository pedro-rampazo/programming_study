"""
- Create 2 dictionaries to read Code(Integer), Number Of Units(Integer) and Price(Float - 2 Decimal Numbers)
- Read Code(Integer), Number Of Units(Integer) and Price(Float - 2 Decimal Numbers) values
- Calculate Value to Pay(Float - 2 Decimal Numbers)
- Print Value to Pay(Float - 2 Decimal Numbers)
- Decimal Numbers syntax: "{:.2f}".format(variable)
"""
product_one = {"code": None, "units": None, "price": None}
product_two = {"code": None, "units": None, "price": None}

print("PRODUCT 1: ")

for key_one, val_one in product_one.items():
    if key_one != "price":
        val_one = int(input(f"Insert {key_one} product: "))
    else:
        val_one = float(input(f"Insert {key_one} product: "))
        val_one = "{:.2f}".format(val_one)
        val_one = float(val_one)
    product_one.update({key_one: val_one})

print("PRODUCT 2: ")

for key_two, val_two in product_two.items():
    if key_two != "price":
        val_two = int(input(f"Insert {key_two} product: "))
    else:
        val_two = float(input(f"Insert {key_two} product: "))
        val_two = "{:.2f}".format(val_two)
        val_two = float(val_two)
    product_two.update({key_two: val_two})

value_to_pay = (product_one.get("price") * product_one.get("units")) + (product_two.get("price") * product_two.get("units"))
value_to_pay = "{:.2f}".format(value_to_pay)

print(f"VALUE TO PAY: R$ {value_to_pay}")

