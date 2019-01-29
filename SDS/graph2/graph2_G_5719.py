#땡
from sys import stdin

MAX = 1000000000

while True:
    N, M = map(int, stdin.readline().split())

    if N == 0 and M == 0:
        break
    S, E = map(int, stdin.readline().split())

    graph = [ [ MAX for _ in range(N) ] for _ in range(N) ]
    
    for m in range(M):
        f, t, w = map(int, stdin.readline().split())
        graph[f][t] = w
        
    for k in range(N):
        for j in range( N):
            for i in range(N):
                if i == j or j == k or i == k:
                    continue
                
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    shortest_path = graph[S][E]
    paths = []
    
    for i in range(N):
        if i == S or i == E:
            continue
        if graph[i][E] == MAX or graph[i][S] == MAX:
            continue
        paths.append(graph[S][i] + graph[i][E])
    
    paths.sort()
    if len(paths) < 1:
        minimum = -1
    else:
        minimum = paths[1]
    
    if minimum == shortest_path or minimum == MAX:
        print(-1)
    else:
        print(minimum)
    