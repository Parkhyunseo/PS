import sys

class Kruskal():
    def __init__(self, f, t, w):
        self.f = f
        self.t = t
        self.w = w
    
    def get(self):
        return (self.f, self.t, self.w)

V, E = map(int, sys.stdin.readline().split())
parent = [ i for i in range(V+1)]
#level = [ 1 for i in range(V+1)]
        
def find(u):
    if u == parent[u]:
        return u
        
    parent[u] = find(parent[u])
    return parent[u]
    
def union(v, u):
    v = parent[v]
    u = parent[u]
    parent[v] = u
    """u = find(u)
    v = find(v)
    
    if u == v:
        return
    
    if level[u] > level[v]:
        u, v = v, u
        
    parent[u] = v
    
    if level[u] == level[v]:
        level[v] += 1
    """
    
kruskals = []
result = 0

cnt = 0
i = 0

for e in range(E):
    A, B, W = map(int, sys.stdin.readline().split())
    kruskals.append(Kruskal(A,B,W))
    
kruskals.sort(key=lambda x: x.w)

while cnt != V-2:
    A, B, W = kruskals[i].get()
    u = find(A)
    v = find(B)
    
    if u != v:
        union(A, B)
        cnt += 1
        result += W
    i+=1
    
print(result)
    
    