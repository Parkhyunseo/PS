N = input()
prices = map(int, raw_input().split())
prices.insert(0, 0)

dp = [ prices[i] for i in xrange(N+1)]

for i in xrange(1, N+1):
    for j in xrange(1, i+1):
        dp[i] = max(prices[j] + dp[i-j], dp[i])
        
print(dp[N])