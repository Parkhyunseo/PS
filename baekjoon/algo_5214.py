from sys import stdin
N, K, M = map(int, stdin.readline().split())

graph = [ [] for _ in range(N+1)]
visitied = [ False for _ in range(N+1)]

for m in range(M):
    hypers = [ int(x) for x in stdin.readline().split() ]
    
    for hyper in hypers:
        graph[hyper].append(hypers)

def bfs():
    if N == 1:
        return 1
        
    q = [ (1, 1) ]
    visitied[1] = True
    
    while len(q) > 0:
        here, count = q.pop(0)
        
        for hyper in graph[here]:
            for there in hyper:
                if here == there:
                    continue
                
                if visitied[there]:
                    continue
                
                if there == N:
                    return count+1
                
                visitied[there] = True
                q.append((there, count+1))
    
    return -1
                
print(bfs())
                    