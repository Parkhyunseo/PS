from sys import stdin 

N, M = map(int, stdin.readline().split())
items = []

for n in range(N):
    V, C, K = map(int, stdin.readline().split())
    items.append((V, C, K))
    
items.sort(lambda x: (x[1], x[0]))

dp = [ [ 0 for _ in range(100001)] for _ in range(N)]

for n in range(N):
    V, C, K = items[n]
    for k in range(K):
        dp[n][k] = min(dp[n][k] )

for i in range(N):
    W, V = items[i]
    for w in range(K+1):
        if w-W >= 0:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-W] + V)
        else:    
            dp[i][w] = dp[i-1][w]

#print(dp)
print(max(dp[N-1]))