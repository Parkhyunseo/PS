N = int(input())
MOD = 15746
dp = [ 0 for _ in range(max(2, N))]
dp[0] = 1
dp[1] = 2

for i in range(2, N):
    dp[i] = (dp[i-1] % MOD + dp[i-2] % MOD) % MOD

print(dp[N-1])