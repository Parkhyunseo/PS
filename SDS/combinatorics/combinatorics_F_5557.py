N = int(input())
form = [ int(x) for x in input().split() ]

# 길이 N인 식으로 K를 만들 수 있는가 (값, 경우의 수)
dp = [ [ 0 for _ in range(21)] for _ in range(N+1) ]

dp[0][0] = 1
dp[1][form[0]] = 1

for n in range(1, N):
    for k in range(21):
        if dp[n][k] == 0:
            continue
        
        if k + form[n] <= 20:
            dp[n+1][k+form[n]] += dp[n][k]
        
        if k - form[n] >= 0:
            dp[n+1][k-form[n]] += dp[n][k]
        

print(dp[N-1][form[-1]])

