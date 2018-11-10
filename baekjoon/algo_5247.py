from queue import Queue

def bfs(s: list): -> int
    x, y = s[0], s[1]
    q = Queue()
    
    for i in range(len(fires)):
        x, y = fires[i]
        q.put((x, y, 0, False))
    q.put((x, y, t, True))
    visit[y][x] = True
    
    while q.qsize() > 0:
        c = q.get()
        cx = c[0]
        cy = c[1]
        ct = c[2]
        cf = c[3]
        
        if cf and ( cx == 0 or cx == M-1 or cy == 0 or cy == N-1):
            return ct + 1
        
        for d in directions:
            nx, ny = cx + d[0] , cy + d[1]
            
            if cx < 0 or cx >= M or cy < 0 or cy >= N):
                continue
            if visit[ny][nx]:
                continue
            if grid[ny][nx] == "*" or grid[ny][nx] == "#":
                continue
           
            if cf:
                visit[ny][nx] = True
            else:
                grid[ny][nx] = False
                
            q.put((nx, ny, ct+1, cf))
                
    return -1
                
T = int(input())
directions = [(0,1),(0,-1),(1,0),(-1,0)]

for t in range(T):
    N, M = map(int, input().split())
    grid = [ [] for _ in range(N)]
    visit = [ [ False for _ in range(M)] for _ in range(N)]
    fires = []
    s = []
    
    for i in range(N):
        line = input().split()
        for j in range(M):
            grid[i].append(line[j])
            if line[j] == '*':
                fires.append((j, i))
            elif line[j] == '@':
                s.append(j)
                s.append(i)
            
    result = bfs(s)
    if result == -1:
        print("IMPOSSIBLE")
    else
        print(result)
                

        
            