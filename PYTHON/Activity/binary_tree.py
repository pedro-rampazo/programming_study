from itertools import count
from platform import node
from unittest import result


binary_tree = [3, 9 20, None, None, 15, 7]
binary_tree = list(filter(None, binary_tree))
lenght_binary_tree = len(binary_tree)
nodes = 0
result = 0

while lenght_binary_tree >= result:
    nodes += 1
    result = 2 ** nodes

print(f"Depth: {nodes}")



