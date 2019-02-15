N = int(input())

cards = [ int(x) for x in input().split() ]

dp = [ 0 for _ in range(N)]

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if cards[j] < cards[i] and dp[j]+1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
    