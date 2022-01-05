"""
Banknotes & Coins
- Read sum_of_money(float - with 2 decimal numbers)
- Create banknotes(dict) → 100, 50, 20, 10, 5, 2
- Create coins(dict) → 1, 0.50, 0.25, 0.10, 0.05, 0.01
- Loop Banknotes
- Loop Coins
"""
banknotes_coins = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
sum_of_money = -1

while sum_of_money <= 0 or sum_of_money > 1000000:
    sum_of_money = int(input("Insert a sum of money: "))

for bnknts_cns in banknotes_coins:
    units = 0
    while sum_of_money >= bnknts_cns:
        sum_of_money -= bnknts_cns
        units += 1
    if units != 0:
        if bnknts_cns > 1:
            print(f"{units} banknote(s) of R$ {'{:.2f}'.format(bnknts_cns)}")
        else:
            print(f"{units} coin(s) of R$ {'{:.2f}'.format(bnknts_cns)}")
