listing = [1, 2, 3]

def SumList(collection):
    if len(collection) == 0:
        return 0
    else:
        return collection[0] + SumList(collection[1:])

print(SumList(listing))
