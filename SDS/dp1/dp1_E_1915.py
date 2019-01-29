N, M = map(int, input().split())

grid = [ [ 0 for _ in range(M)] for _  in range(N)]
dp = [ [ 0 for _ in range(M)] for _  in range(N)]

result = 0

for i in range(N):
    line = list(input())
    for j in range(M):
        if line[j] == '1':
            dp[i][j] = 1
            result = 1
        grid[i][j] = line[j]
            

for i in range(1, N):
    for j in range(1, M):
        if grid[i-1][j-1] == '1' and grid[i-1][j] == '1' and grid[i][j-1] == '1':
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
             
        result = max(dp[i][j], result)
            
print(result*result)