from sys import stdin, stdout

class Node():
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

root = None

for value in stdin.readlines():
    value = int(value)
    if root == None:
        root = Node(value)
        continue
    
    node = root
    while True:
        if  value > node.value:
            if node.right != None:
                node = node.right
            else:
                node.right = Node(value, parent=node)
                break
        else:
            if node.left != None:
                node = node.left
            else:
                node.left = Node(value, parent=node)
                break
            
def postorder(node):
    if node == None:
        return
    
    postorder(node.left)
    postorder(node.right)
    stdout.write(str(node.value)+'\n')
    
postorder(root)
            