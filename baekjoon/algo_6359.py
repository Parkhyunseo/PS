T = int(input())
for t in range(T):
    N = int(input())
    dp = [ True for _ in range(N+1)]
    for i in range(2, N+1):
        for j in range(i, N+1, i):
            dp[j] = not dp[j]
            
    print(dp.count(True)-1)