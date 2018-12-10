N, M = map(int, input().split())

maze = [ [ 0 for col in range(M+1) ] for row in range(N+1)]
dp = [ [ 0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    maze[i] = [0]
    maze[i].extend([ int(x) for x in input().split() ])

for i in range(1, N+1):
    for j in range(1, M+1):
        result = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        dp[i][j] = result + maze[i][j]
        
print(dp[N][M])
