from sys import stdin

N, M = map(int, stdin.readline().split())

base = [ [0] for _ in range(N+1)]
# dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + base[i][j]
dp = [ [ 0 for _ in range(N+1)] for _ in range(N+1)]

base[0] = [ 0 for _ in range(N+1)]

for n in range(1, N+1):
    base[n].extend([int(x) for x in stdin.readline().split()])

for i in range(1, N+1):
    for j in range(1, N+1):
         dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + base[i][j]

for m in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])