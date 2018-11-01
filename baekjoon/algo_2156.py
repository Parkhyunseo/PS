N = input()
wines = []
dp = [ 0 for _ in range(N)]

for n in range(N):
    wines.append(input())

dp[0] = wines[0]
dp[1] = wines[0] + wines[1] 
dp[2] = max(wines[0] + wines[1] , wines[1] + wines[2], wines[0]+ wines[2])

for n in range(3, N):
    dp[n] = max(dp[n-2] + wines[n], dp[n-3] + wines[n] + wines[n-1]) 
    
print(dp[N-1])
