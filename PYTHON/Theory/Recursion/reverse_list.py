listing = [1, 2, 3]

def ReverseList(collection):
    if len(collection) == 0:
        return collection
    return collection[-1:] + ReverseList(collection[:-1])

print(ReverseList(listing))