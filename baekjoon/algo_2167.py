from sys import stdin
N, M = map(int, stdin.readline().split())
grid = [ [ 0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    data = list(map(int, stdin.readline().split()))
    for j in range(1, M+1):
        grid[i][j] = grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1] + data[j-1]

T =int(input())
for t in range(T):
    j,i,y,x = map(int, stdin.readline().split())
    result = grid[y][x] - grid[y][i-1] - grid[j-1][x] + grid[i-1][j-1]
    print(result)