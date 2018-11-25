from sys import stdin

N, S = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))
calcum = [ 0 for _ in range(N)]
calcum[0] = A[0]
result = 0

for i in range(1, N):
    calcum[i] = calcum[i-1] + A[i]

result = 100000001
for i in range(1, N):
    for j in range(i):
        if calcum[i] - calcum[j-1] >= S:
            result = min(result, i-j+1)
    
print(result)