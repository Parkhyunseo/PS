N = int(input())
MAX = 1000000000000
maze = [ int(x) for x in input().split()]

# dp[i] i번째에 뛰어서 왔을때 최소 점프 횟수
dp = [ MAX for _ in range(N)]
dp[0] = 0

for i in range(N):
    for j in range(maze[i]+1):
        if i+j < N:
            dp[i+j] = min(dp[i+j], dp[i] + 1)

if dp[-1] == MAX:
    print(-1)
else:
    print(dp[-1])
        