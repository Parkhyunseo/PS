N = int(input())

dp = [ 1 for _ in range(max(4,N))]
dp[2]= 2

for i in range(3, N):
    dp[i] = dp[i-1]+dp[i-3]

print(dp[N-1]%1000000009)