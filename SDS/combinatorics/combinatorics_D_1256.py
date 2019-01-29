N,M,K=map(int,input().split())
MAX = 1000000001
LEN = N+M

# dp[A][B] 길이 A의 문자열중에 a가 A개 들어있는?
dp = [ [ 0 for _ in range(LEN+1)] for _ in range(LEN+1) ]
dp[0][0] = 1
for n in range(1, LEN+1):
    dp[n][0] = 1
    for k in range(LEN+1):
        # C언어라면 min(dp[n-1][k-1] + dp[n-1][k], MAX)
        dp[n][k] = min(dp[n-1][k-1] + dp[n-1][k], MAX)

if dp[LEN][N] < K:
    print(-1)
else:
    s = ''
    for _ in range(LEN):
        if dp[N+M-1][M] < K:
            s += 'z'
            K -= dp[N+M-1][M]
            M -= 1
        else:
            s += 'a'
            N -= 1
            
    print(s)