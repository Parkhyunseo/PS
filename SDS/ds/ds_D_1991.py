N = int(input())

class Node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

tree = [ 0 for _ in range(27)]
for i in range(N):
    p, l, r = input().split()
    tree[ord(p)-ord('A')] = Node(p, l, r)
    
def preorder(node):
    if tree[node].value == '.':
        return
    
    print(tree[node].value, end='')
    
    if tree[node].left != '.':
        preorder(ord(tree[node].left)-ord('A'))
    
    if tree[node].right != '.':
        preorder(ord(tree[node].right)-ord('A'))

def inorder(node):
    if tree[node].value == '.':
        return
    
    if tree[node].left != '.':
        inorder(ord(tree[node].left)-ord('A'))
        
    print(tree[node].value, end='')
    
    if tree[node].right != '.':
        inorder(ord(tree[node].right)-ord('A'))
        
def postorder(node):
    if tree[node].value == '.':
        return
    
    if tree[node].left != '.':
        postorder(ord(tree[node].left)-ord('A'))
    
    if tree[node].right != '.':
        postorder(ord(tree[node].right)-ord('A'))
    
    print(tree[node].value, end='')
    
preorder(0)
print('')
inorder(0)
print('')
postorder(0)
print('')
    
    
    
    