from queue import Queue

M, N = map(int, input().split())
box = [ [] for _ in range(N)]
visited = [ [ False for _ in range(M)] for _ in range(N)]
direction = [(0,1), (1,0), (-1,0), (0, -1)]

count = 0

q = Queue()

for n in range(N):
    line = [ int(x) for x in input().split()]
    for m in range(M):
        if line[m] is 1:
            q.put((m, n, 0))
    box[n] = line
    

while q.qsize() > 0:
    x, y, c = q.get()
    
    box[y][x] = 1
    count = max(c, count)
    
    for d in direction:
        nx = x + d[0]
        ny = y + d[1]
        
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
    
        if visited[ny][nx]:
            continue
        
        if box[ny][nx] == -1:
            continue
        
        visited[ny][nx] = True
        q.put((nx, ny, c+1))
        

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit()

print(count)
    
            
        
        