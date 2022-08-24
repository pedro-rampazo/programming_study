def Potentiation(base, n):
    print(f"{base} ** {n} = {base ** n}")
    if n > 0:
        Potentiation(base, n - 1)

Potentiation(2, 10)