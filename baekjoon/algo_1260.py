from sys import stdin
from queue import Queue

N, M, V = map(int, stdin.readline().split())
graph = [ [ 0 for _ in range(N+1) ] for _ in range(N+1)]
visited = [ False for _ in range(N+1)]

def bfs(v):
    result = []
    
    q = Queue()
    q.put(v)
    visited[v] = False
    
    while q.qsize() > 0:
        here = q.get()
        print(here, end=" ")

        for there in range(1, N+1):
            if graph[here][there] == 1 and visited[there]:
                visited[there] = False
                q.put(there)
                    
    return result

def dfs(here):
    visited[here] = True
    print(here, end=" ")
    
    for there in range(1, N+1):
        if graph[here][there] == 1 and not visited[there]:
            dfs(there)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
dfs(V)
print("")
bfs(V)
print("")