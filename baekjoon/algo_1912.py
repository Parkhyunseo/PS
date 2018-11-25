N = int(input())
dp = [ int(x) for x in input().split()]
result = dp[0]

for i in range(1, N):
    if dp[i-1] > 0 and dp[i] + dp[i-1] > 0:
        dp[i] += dp[i-1]
    
    result = max(dp[i], result)
print(result)

#모두 음수일 경우 안돼