from tree_module import *

tree = BinaryTree(7)
tree.root.left = Node(18)
tree.root.right = Node(14)

print(tree.root)
print(tree.root.right)
print(tree.root.left)
