# N = 500
# N^3 가능
from sys import stdin

N, M = map(int, stdin.readline().split())
MAX = 10000

realtions = [ [ MAX  for _ in range(N+1)] for _ in range(N+1) ]
degree = [ 0 for _ in range(N+1)]

for m in range(M):
    f, t = map(int, stdin.readline().split())
    
    realtions[f][t] = 1
    
for k in range(1, N+1):
    for j in range(1, N+1):
        for i in range(1, N+1):
            if realtions[i][j] > realtions[i][k] + realtions[k][j]:
                realtions[i][j] = realtions[i][k] + realtions[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if realtions[i][j] != MAX:
            degree[i] += 1
            degree[j] += 1
result = 0            
for i in range(1, N+1):
    if degree[i] == N-1:
        result += 1
        
print(result)