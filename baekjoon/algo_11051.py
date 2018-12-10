MOD = 10007
N, K = map(int, input().split())

dp = [ [ 0 for _ in range(K+1)] for _ in range(N+1)]

for n in range(1, N+1):
    for k in range(K+1):
        if n == k or k == 0:
            dp[n][k] = 1
            continue
        dp[n][k] = (dp[n-1][k]%MOD + dp[n-1][k-1]%MOD)%MOD
        
print(dp[N][K])