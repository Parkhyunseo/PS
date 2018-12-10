# 3 
N = int(input())

dp = [ 0 for _ in range(31)]
dp[0] = 1

for i in range(2, N+1, 2):
    dp[i] = 3*dp[i-2]
    for j in range(4, i+1, 2):
        dp[i] += 2 * dp[i-j]
        
print(dp[N])