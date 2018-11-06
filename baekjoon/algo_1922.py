import sys

class Kruskal():
    def __init__(self, f, t, w):
        self.f = f
        self.t = t
        self.w = w
    
    def get(self):
        return (self.f, self.t, self.w)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
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
        
kruskals = []
result = 0

for m in range(M):
    A, B, W = map(int, sys.stdin.readline().split())
    kruskals.append(Kruskal(A, B, W))
    
kruskals.sort(key=lambda x : x.w)

for k in kruskals:
    A, B, W = k.get()
    u = find(A)
    v = find(B)
    
    if u != v:
        union(A, B)
        result += W
        
print(result)
    
    