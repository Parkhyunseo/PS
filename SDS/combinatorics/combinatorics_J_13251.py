M = int(input())
colors = [int(x) for x in input().split()]
MAX = sum(colors)
K = int(input())

dp = [ [ 0 for _ in range(MAX+1)] for _ in range(MAX+1) ]
dp[0][0] = 1
for n in range(1, MAX+1):
    dp[n][0] = 1
    for k in range(MAX+1):
        dp[n][k] = dp[n-1][k-1] + dp[n-1][k]
        
result = 0
for color in colors:
    if color >= K:
        result += dp[color][K]
        
print(result/dp[MAX][K])