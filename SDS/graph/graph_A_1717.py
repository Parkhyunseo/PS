from sys import stdin

N, M = map(int, input().split())

parent = [ i for i in range(N+1)]
rank = [ 0 for _ in range(N+1)]

def find(x):
    if x == parent[x]:
        return x
        
    parent[x] = find(parent[x])
    return parent[x]
    
def union(v, u):
    pv, pu = find(v), find(u)
    
    if pv == pu:
        return
    
    if rank[pu] > rank[pv]:
        pv, pu = pu, pv
        
    parent[pu] = pv
    
    if rank[pu] == rank[pv]:
        rank[pv] += 1
        

for i in range(M):
    query, a, b = map(int, stdin.readline().split())
    
    if query == 0:
        union(a, b)
    else:
        pa = find(a)
        pb = find(b)
        
        if pa == pb:
            print("YES")
        else:
            print("NO")
        
        
    
    

    