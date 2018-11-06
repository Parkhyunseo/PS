import sys

N,M = map(int, sys.stdin.readline().split())
parent = [ i for i in range(N+1)]
level = [ 1 for i in range(N+1)]
        
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

for i in range(M):
    op, a, b = map(int, sys.stdin.readline().split())
    
    if op == 0:
        union(a, b)
    else:
        r1 = find(a)
        r2 = find(b)
        if r1 == r2:
            print("YES")
        else:
            print("NO")