N = int(input())
A = list(map(int, input().split()))
DP = [ 1 for _ in range(N) ]

for i in range(N):
    for j in range(N):
        if i > j and A[i] > A[j]:
            DP[i] = max(DP[i], DP[j]+1)
        elif i < j and A[i] < A[j]:
            DP[i] = max(DP[i], DP[j]+1)
            
print(DP)
        
        