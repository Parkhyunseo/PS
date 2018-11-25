from sys import stdin

N = int(input())
A = list(map(int, stdin.readline().split()))
M = int(input())

calcum = [ 0 for _ in range(N+1)]
calcum[1] = A[0]
result = 0

for i in range(2, N+1):
    calcum[i] = calcum[i-1] + A[i-1]

for i in range(M):
    S, E= map(int, stdin.readline().split())
    print(calcum[E]-calcum[S-1])
    