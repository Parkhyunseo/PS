N, K = map(int, input().split())
color = [ int(x) for x in input().split()]

dp = [ [ 99999999 for _ in range(N+1)] for _ in range(N+1)]

# O(N^3)
for j in range(N):
    for i in range(j, -1, -1):
        if i == j:
            dp[i][j] = 0
            continue
        
        for k in range(i, j):
            if color[i] != color[k+1]:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + 1)
            else:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

for i in range(N):
    print(dp[i])

print(dp[0][N-1])