import sys

class Edge():
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight
        
    def get(self):
        return (self.start, self.end, self.weight)

N = int(input())
M = int(input())
ans = 0

edges = []
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
    s, e, w = map(int, sys.stdin.readline().split())
    edges.append(Edge(s, e, w))
    
edges.sort(key=lambda x:x.weight)

for edge in edges:
    s, e, w = edge.get()
    
    s = find(s)
    e = find(e)
    
    if s != e:
        union(s, e)
        ans += w
        
print(ans)
    