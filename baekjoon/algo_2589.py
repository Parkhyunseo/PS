import sys

H, W = map(int, sys.stdin.readline().split())
grid = []
direction = [(0,1), (0,-1), (1,0), (-1, 0)]

for i in range(H):
    grid.append(list(sys.stdin.readline())[:-1])
    
def bfs(sx, sy):
    if grid[sy][sx] == 'W':
        return
    
    q = []
    q.append((sx, sy, 0))
    
    visit = [ [False for _ in range(W) ] for _ in range(H)] 
    visit[sy][sx] = True
    
    while len(q) > 0:
        cx, cy, count = q.pop(0)
        min_dist[cy][cx] = max(min_dist[cy][cx], count)
        
        for d in direction:
            nx = cx + d[0]
            ny = cy + d[1]
            
            if nx < 0 or nx >= W or ny < 0 or ny >= H :
                continue
            
            if visit[ny][nx]:
                continue
            
            visit[ny][nx] = True
            
            if grid[ny][nx] == 'L':
                q.append((nx, ny, count+1))
                
min_dist = [ [-1 for _ in range(W) ] for _ in range(H)]

for y in range(H):
    for x in range(W):
        bfs(x, y)

result = 0
for y in range(H):
    for x in range(W):
        result = max(result, min_dist[y][x])
                
print(result)