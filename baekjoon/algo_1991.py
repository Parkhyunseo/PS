N = input()
tree = [ 0 for _ in range(N)]

for i in range(1, N):
    parent, left, right = raw_input().split()
    tree[i] = parent
    if left != '.':
        tree[i*2 + 1] = left
    if right != '.':
        tree[i*2 + 2] = right
    
print tree