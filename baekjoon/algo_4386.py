import sys

N = int(input())
parent = [ i for i in range(N)]
rank = [ 1 for i in range(N)]
stars = []

class Kruskal:
    def __init__(self, f, t, w):
        self.f = f
        self.t = t
        self.w = w
        
    def get(self):
        return (self.f, self.t, self.w)

def distance(a, b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

def find(u):
    if u == parent[u]:
        return u
        
    parent[u] = find(parent[u])
    return parent[u]
    
def union(u, v):
    u = find(u)
    v = find(v)
    
    if u == v:
        return
    
    if rank[u] > rank[v]:
        u, v = v, u
        
    parent[u] = v
    
    if rank[u] == rank[u]:
        rank[v] += 1
    

kruskals = []

for n in range(N):
    stars.append(tuple(map(float, sys.stdin.readline().split())))
    
for i in range(N-1):
    for j in range(i+1, N):
            kruskals.append(Kruskal(i, j, distance(stars[i], stars[j])))
            
kruskals.sort(key=lambda x:x.w)

result = 0
cnt = 0

for i in range(len(kruskals)):
    f, t, w = kruskals[i].get()
    
    f = find(f)
    t = find(t)
    
    if f != t:
        union(f, t)
        result += w
        cnt += 1
        
    if cnt == N-1:
        break
        
print("%.2f" % result)
        
    