import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

class Node:
    def __init __(self, f, t ,w):
        self.f = f
        self.t = t
        self.w = w
    

result = [] 

while True:
    N, M = map(int, input().split())
    grid= [ [ 0 for _ in range(N) ] for _ in range(N)]
    
    if N == 0 and M == 0:
        break
    
    S, D = map(int, input().split())
    
    for m in range(M):
        f, t, w = map(int, input().split())
        grid[f][t] = w
        #grid[t][f] = -w
        
        
def dijkstra(N, S, D):
    weights = [ 0 for _ in range(N)]
    q = PriorityQueue()
    q.put(S)
    
    while q.qsize() > 0:
        val = q.get()
        
    
    