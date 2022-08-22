'''
BINARY TREE:

Concepts:
- Root: first value in a tree
- Leaf: last value that don't have sons
- Son: When one value is a direct descendant of another
- Descendant: When a value is an indirect descendant of another value

Minimun Height: h(N) min = 1 + Log N(2) -> K <= X < K+1
Maximun Height: h(N) max = N
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
    
    
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')

    
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)

    counter = 0
    max_height = 0

    def height(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.counter += 1
            self.height(node.left)
        if node.right:
            self.counter += 1
            self.height(node.right)
        if self.counter > self.max_height:
            self.max_height = self.counter
        self.counter -= 1
        
        