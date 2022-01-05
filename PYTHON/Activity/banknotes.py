"""
DATA
- Banknotes: 100, 50, 20, 10, 5, 2, 1
- Input Integer N (0 < N < 1.000.000)

SCRIPT
- banknotes(list) with banknotes values
- units(int)
- Read sum_of_money(int)
    → 0 < sum_of_money < 1.000.000
- Loop FOR to get banknote one by one
    → Loop WHILE to get banknotes units
    → print units and banknote value 
"""
banknotes = [100, 50, 20, 10, 5, 2, 1]
sum_of_money = -1
units = 0

while sum_of_money <= 0 or sum_of_money > 1000000:
    sum_of_money = int(input("Insert a sum of money: "))

for val in banknotes:
    while sum_of_money >= val:
        sum_of_money -= val
        units += 1
    if units != 0:
        print(f"{units} banknote(s) of R$ {'{:.2f}'.format(val)}")
    units = 0
