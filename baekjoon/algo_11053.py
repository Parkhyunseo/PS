#import bisect

N = int(input())
A = list(map(int, input().split()))
DP = [ 1 for _ in range(N) ] 

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))
    