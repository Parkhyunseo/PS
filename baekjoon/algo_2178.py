from sys import stdin
H, W = map(int, stdin.readline().split())
arr = []

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for y in range(H):
    line = [ int(x) for x in stdin.readline()[:-1]]
    arr.append(line)
    
def bfs(sx, sy):
    q = []
    result = 0
    
    q.append((sx, sy, 1))
    
    visit = [ [ False for _ in range(W)] for _ in range(H)]
    visit[sy][sx] = True
    
    while len(q) > 0:
        cx, cy, distance = q.pop(0)
        
        if (cx == W-1) and (cy == H-1):
            result = distance
            break
        
        for d in direction:
            nx = cx + d[0]
            ny = cy + d[1]
            
            if nx < 0 or nx >= W or ny < 0 or ny >= H or (visit[ny][nx] == True):
                continue
            
            if arr[ny][nx] == 0:
                continue
            
            if visit[ny][nx]:
                continue
            
            visit[ny][nx] = True
            q.append((nx, ny, distance+1))
            
    return result

answer = bfs(0, 0)
if answer != 0:
    print(answer)