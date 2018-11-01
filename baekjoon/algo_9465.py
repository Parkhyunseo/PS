T = input()

for t in range(T):
    N = input()
    sticker = [ [] for _ in range(2) ]
    sticker[0] = map(int, raw_input().split())
    sticker[1] = map(int, raw_input().split())
    dp = [ [ 0 for _ in range(N)] for _ in range(3) ]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[2][0] = 0
    
    for n in range(1, N):
        dp[0][n] = max(dp[1][n-1] + sticker[0][n], dp[2][n-1] + sticker[0][n])  
        dp[1][n] = max(dp[0][n-1] + sticker[1][n], dp[2][n-1] + sticker[1][n])
        dp[2][n] = max(dp[0][n-1], dp[1][n-1], dp[2][n-1])
    
    print(max(dp[0][N-1], dp[1][N-1], dp[2][N-1]))