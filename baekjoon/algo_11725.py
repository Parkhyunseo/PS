from sys import stdin
from queue import Queue

N = int(input())
graph = [ [] for _ in range(N)]
visit = [ False for _ in range(N)]
parent = [ 0 for _ in range(N)]

for n in range(N-1):
    f, t = map(lambda x: int(x)-1, stdin.readline().split())
    graph[f].append(t)
    graph[t].append(f)
    
q = Queue()
q.put(0)

while q.qsize() > 0:
    here = q.get()
    visit[here] = True
    
    for j in range(len(graph[here])):
        there = graph[here][j]
        
        if not visit[there]:
            parent[there] = here
        
            q.put(there)
     
for p in parent[1:]:
    print(p+1)
        
    

