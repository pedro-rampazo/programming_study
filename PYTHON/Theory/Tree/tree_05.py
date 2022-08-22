from tree_module import *

tree = BinaryTree()
n1 = Node('a')
n2 = Node('b')
n3 = Node('c')
n4 = Node('d')
n5 = Node('e')
n6 = Node('f')
n7 = Node('g')
n8 = Node('h')

n6.left = n8
n3.left = n6
n3.right = n7
n2.left = n4
n2.right = n5
n1.left = n2
n1.right = n3
tree.root = n1

print(f"Height: {tree.height()}")
