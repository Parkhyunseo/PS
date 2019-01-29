from sys import stdin

MAX = 1000000000

N = int(input())
M = int(input())

graph = [ [ MAX for _ in range(N+1) ] for _ in range(N+1) ]

for m in range(M):
    f, t, w = map(int, stdin.readline().split())
    
    graph[f][t] = min(graph[f][t], w)
    
for k in range(1, N+1):
    for j in range(1, N+1):
        for i in range(1, N+1):
            if i == j or j == k or i == k:
                continue
            
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == MAX:
            print("0", end=" ")
        else:
            print(graph[i][j], end=" ")
    print("")

    