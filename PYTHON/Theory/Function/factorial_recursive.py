def recursiveS(intern_numberS):
    factorial = 1
    if intern_numberS == 0:
        return 1
    else:
        for nmbr in range(1, intern_numberS + 1):
            factorial *= nmbr
        return factorial

print(recursiveS(3))


def recursiveR(intern_numberR):
    if intern_numberR == 0: #function call termination
        return 1
    else:
        return intern_numberR * recursiveR(intern_numberR - 1) # call recursiveS() function again

print(recursiveR(3))