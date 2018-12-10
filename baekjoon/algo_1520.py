from sys import stdin
M, N = map(int, stdin.readline().split())
grid =  [ []for _ in range(M)]
dp = [ [-1 for _ in range(N)] for _ in range(M)]
ds = [ (1,0), (0,1), (-1, 0), (0,-1)]
fbd = [2, 3, 0, 1]

for i in range(M):
    grid[i] = [ int(x) for x in stdin.readline().split() ]
 
def solve(d, x, y):
    if y == M-1 and x == N-1:
        return 1
    elif dp[y][x] == -1:
        dp[y][x] = 0
        for i in range(len(ds)):
            if fbd[d] != i:
                nx = x + ds[i][0]
                ny = y + ds[i][1]
                
                if nx >= 0 and nx < N and ny >=0 and ny < M:
                    if grid[y][x] > grid[ny][nx]:
                        dp[y][x] += solve(i, nx, ny)
    
    return dp[y][x]
    
        

print(solve(1, 0, 0))