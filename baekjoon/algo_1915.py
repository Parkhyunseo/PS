N, M = map(int, input().split())
grid = [ [] for _ in range(N) ]
dp = [ [ 0  for _ in range(M) ] for _ in range(N)]

for h in range(N):
    grid[h] = [ int(x) for x in list(input()) ] 
    
for i in range(1, N):
    for j in range(1, M):
        if grid[i][j] == 1:
            if grid[i][j-1] == grid[i-1][j]:
                k = grid[i][j-1]
                if grid[i-k][j-k] != 0:
                    grid[i][j] = grid[i][j-1] + 1
                else:
                    grid[i][j] = grid[i][j-1] - 1
            else:
                k = min(grid[i][j-1], grid[i-1][j])
                grid[i][j] = k + 1
            
for x in grid:
    print(x)

            
    

    