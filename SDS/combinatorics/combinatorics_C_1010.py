T = int(input())

MAX = 30

dp = [ [ 0 for _ in range(MAX)] for _ in range(MAX)]

dp[0][0] = 1

for n in range(1, MAX):
    dp[n][0] = 1
    for k in range(MAX):
        dp[n][k] = dp[n-1][k-1] + dp[n-1][k]

for t in range(T):
    N, K = map(int, input().split())
    
    if K > N:
        N, K = K, N
        
    print(dp[N][K])