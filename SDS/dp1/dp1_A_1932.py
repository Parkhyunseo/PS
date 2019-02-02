N=int(input())

tri = []
dp = [ [ 0 for _ in range(i+1) ] for i in range(N) ]

for i in range(N):
    tri.append([int(x) for x in input().split()])
    
for l in range(N):
    dp[l][0]=dp[l-1][0] + tri[l][0]
    
    if l >= 1:
        dp[l][l] = dp[l-1][l-1] + tri[l][l]
    if l >= 2:
        for i in range(1, l):
            dp[l][i] = max(dp[l-1][i-1], dp[l-1][i]) + tri[l][i]
            
print(max(dp[N-1]))