import sys

class Kruskal():
    def __init__(self ,f, t, w):
        self.f = f
        self.t = t
        self.w = w
        
    def get(self):
        return (self.f, self.t, self.w)

def find(u:int) -> int:
    if u == parent[u]:
        return u
    
    parent[u] = find(parent[u])
    return parent[u]
    
def union(u:int , v:int):
    u = find(u)
    v = find(v)
    
    if u == v:
        return
    
    if rank[u] > rank[v]:
        u, v = v, u
    
    parent[u] = v
    
    if rank[u] == rank[v]:
        rank[v] += 1

while True:
    V, E = map(int, sys.stdin.readline().split())

    if V == 0 and E == 0:
        break
    
    edges = []
    total = 0
    use = 0

    parent = [ i for i in range(V)]
    rank = [ 1 for _ in range(V)]
    
    for i in range(E):
        f, t, w = map(int, sys.stdin.readline().split())
        edges.append(Kruskal(f, t, w))
        total += w
    
    edges.sort(key=lambda x:x.w)
    count = 0
    
    for edge in edges:
        f, t, w = edge.get()
        
        f = find(f)
        t = find(t)
        if f != t:
            union(f, t)
            use += w
            count += 1
            if count >= V-1:
                break
    
    print(total - use)