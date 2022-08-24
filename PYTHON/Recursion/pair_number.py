listing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def PairNumber(collection):
    if len(collection) == 0:
        return collection
    if collection[0] % 2 == 0:
        return collection[0:1] + PairNumber(collection[1:])
    else:
        PairNumber(collection[1:])

print(PairNumber(listing))