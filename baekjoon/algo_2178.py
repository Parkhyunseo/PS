from queue import Queue

H, W = map(int, input().split())
arr = []

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for y in range(H):
    arr.append(list(map(int, list(input()))))
    
def bfs(sx, sy):
    q = Queue(W*H)
    result = 0
    
    q.put((sx, sy, 1))
    
    visit = [ [ False for _ in range(W)] for _ in range(H)]
    
    while q.qsize() > 0:
        cx, cy, distance = q.get()
        visit[cy][cx] = True
        
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
            
            q.put((nx, ny, distance+1))
            
    return result

answer = bfs(0, 0)
if answer != 0:
    print(answer)