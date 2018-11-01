import sys
from queue import Queue

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visit = None

def bfs(sx, sy):
    global count
    
    q = Queue()
    q.put((sx, sy))

    while q.qsize() > 0:
        cx, cy = q.get()
        visit[cy][cx] = True
        
        for d in direction:
            nx = cx+d[0]
            ny = cy+d[1]
            
            if nx < 0 or nx >= M or ny < 0 or ny >= N or visit[ny][nx] == True:
                continue
            
            if grid[ny][nx] == 1:
                q.put((nx, ny))
                
    count += 1


T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    grid = [ [ 0 for _ in range(M)]  for _ in range(N)]
    visit = [ [False for _ in range(M) ] for _ in range(N)]
    count = 0
    
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        grid[y][x] = 1
        
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1 and visit[y][x] == False:
                bfs(x, y)
            #print(visit)
                #count += 1
                
    print(count)
