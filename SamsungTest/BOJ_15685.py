N = int(input())

# 0

# 0 3

# 0 3 2 3

# 0, 3, 2, 3, 2, 1, 2, 3

# 끝점 기준으로 시계방향 90도 회전시키기 때문에
# 끈점 기준으로 한칸 갈 때마다 
#    이전 세대  <- [끝점] -> 새로운 세대
# 라고 할 때 한칸씩움직이며 이전 세대의 방향에 90도 회전 시키면된다.
#먼저 dp를만들자
# dp[x][y] x 새대에 y번째는 어느 방향으로 움직이나
# 정사각형의 개수는 for문 돌면서 확인

def curve(x, y, d, g):
    pass

for i in range(N):
    x, y, d, g = map(int, input().split())
    curve(x, y, d, g)
    
# 입력 최솟값 + 1부터 어디까찌
grid = [ [] ]
count = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] == 1 and grid[i+1][j] == 1 and grid[i][j+1] == 1 and grid[i+1][j+1] == 1:
            count += 1
