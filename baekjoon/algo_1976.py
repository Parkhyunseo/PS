import sys 

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

travel = []

parent = [ i for i in range(N)]
level = [ 1 for i in range(N)]
        
def find(u):
    if u == parent[u]:
        return u
        
    parent[u] = find(parent[u])
    return parent[u]
    
def union(v, u):
    u = find(u)
    v = find(v)
    
    if u == v:
        return
    
    if level[u] > level[v]:
        u, v = v, u
        
    parent[u] = v
    
    if level[u] == level[v]:
        level[v] += 1

for i in range(N):
    travel.append(list(map(int, sys.stdin.readline().split())))
quiz = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    for j in range(N):
        if travel[i][j] == 1:
            union(i, j)
c = False
before = find(quiz[0]-1)

for q in range(1, M):
    u = find(quiz[q]-1)
    if before != u:
        c = True
        break
    before = u
    
if c:
    print("NO")
else:
    print("YES")
    
    
    

