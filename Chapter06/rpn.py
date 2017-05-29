from stack import Stack

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

def calc(node):
    if node.data is "+":
        return calc(node.left) + calc(node.right)
    elif node.data is "-":
        return calc(node.left) - calc(node.right)
    elif node.data is "*":
        return calc(node.left) * calc(node.right)
    elif node.data is "/":
        return calc(node.left) / calc(node.right)
    else:
        return node.data

expr = "4 5 + 5 3 - *".split()
stack = Stack()

for term in expr:
    if term in "+-*/":
        node = TreeNode(term)
        node.right = stack.pop()
        node.left = stack.pop()
    else:
        node = TreeNode(int(term))
    stack.push(node)

root = stack.pop()
result = calc(root)
print(result)
