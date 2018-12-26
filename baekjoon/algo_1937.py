N = int(input())
bambus = []
dp = [ [ 0 for _ in range(N)] for _ in range(N)]
direction = [(0,1), (0,-1), (1, 0), (-1, 0)]

ans = 0
count = 0
for i in range(N):
    bambus.append([ int(x) for x in input().split() ])

def dfs(y, x):
    global dp
    global ans
    
    value = 0
    for d in direction:
        nx = x + d[0]
        ny = y + d[1]
                
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        
        if bambus[ny][nx] > bambus[y][x]:
            if dp[ny][nx] == 0:
                dfs(nx, ny)
                
            if value < dp[ny][nx]:
                value = dp[ny][nx]
    
    dp[y][x] = value + 1
    
    if ans < dp[y][x]:
        ans = dp[y][x]
            
for i in range(N):
    for j in range(N):
        if dp[i][j] == 0:
            dfs(i, j)
print(ans)