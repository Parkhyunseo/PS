from sys import stdin 

N, K = map(int, stdin.readline().split())
items = []

for n in range(N):
    W, V = map(int, stdin.readline().split())
    items.append((W,V))
    
dp = [ [ 0 for _ in range(K+1)] for _ in range(N)]
    
for i in range(N):
    W, V = items[i]
    for w in range(K+1):
        if w-W >= 0:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-W] + V)
        else:    
            dp[i][w] = dp[i-1][w]

#print(dp)
print(max(dp[N-1]))