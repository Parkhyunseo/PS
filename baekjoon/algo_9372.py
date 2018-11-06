import sys

T = int(input())
"""
def make_set(v):
    parent[v] = v
    rank[v] = 0
    
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]
    
def union(v, u):
    root1 = find(v)
    root2 = find(u)
    
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(graph, N):
    for v in range(N):
        make_set(v)
        
    mst = []
    
    for edge in range(N):
        weigh, v, u = edge 
        
        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
            
    return mst
"""
from queue import Queue

def bfs(s):
    q = Queue()
    q.put((s, 0))
    visit = [ False for _ in range(N) ]
    result = 0
    
    while q.qsize() > 0:
        c, count = q.get()
        result = count
        visit[c] = True
        
        for nei in air[c]:
            if not visit[nei]:
                q.put((nei, count+1))
            
    return result

for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    air = [[] for _ in range(N)]
    
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        air[a-1].append(b-1)
        air[b-1].append(a-1)
        
    #count = bfs(0)
    
    print(N-1)