import bisect

N = int(input())
A = list(map(int, input().split()))
B = [-A[0]]

# dp[i][j]
# dp[i-1]
for i in range(N):
    if B[-1] < -A[i]:
        B.append(-A[i])
    else:
        idx = bisect.bisect_left(B, -A[i], 0, len(B))
        B[idx] = -A[i]
    
print(B)