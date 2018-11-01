N, M = map(int, input().split())

D = [ 0 for _ in range(N) ]
order = [ 0 for _ in range(N) ]
deg = [ 0 for _ in range(N) ]
con = [ [] for _ in range(N) ]

for i in range(M):
    a, b = map(int, input().split())
    
    deg[a] += 1
    deg[b] += 1
    
    con[a].append(b)
    con[b].append(a)

for i in range(N):
    order[i] = i
    
order.sort(key=lambda x: order.index())
    
    