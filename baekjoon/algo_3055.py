R, C = map(int, input().split())

directions = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
visited = [ [ False for _ in range(C)] for _ in range(R)]
grid = []
waters = []

start = (0, 0)

for r in range(R):
    line = list(input())
    for c in range(C):
        if line[c] == 'S':
            start = (c, r)
        elif line[c] == '*':
            waters.append((c, r))
            
    grid.append(line)
            
q = []
for water in waters:
    x, y = water
    q.append(('*', x, y, 0))
    
q.append(('S', start[0], start[1], 0))

answer = 'KAKTUS'

while len(q) > 0:
    csign, cx, cy, count = q.pop(0)
    
    for d in directions:
        nx = cx + d[0]
        ny = cy + d[1]
    
        if nx < 0 or nx >= C or ny < 0 or ny >= R:
            continue
        
        if grid[ny][nx] == '*':
            continue
        elif grid[ny][nx] == 'D':
            if csign == '*':
                continue
            elif csign == 'S':
                answer = count + 1
                break
        elif grid[ny][nx] == 'S':
            if csign == '*':
                grid[ny][nx] = '*'
                q.append((csign, nx, ny, count+1))
            elif csign == 'S':
                continue
        elif grid[ny][nx] == '.':
            if csign == '*':
                grid[ny][nx] = '*'
            elif csign == 'S':
                grid[ny][nx] = 'S'
            q.append((csign, nx, ny, count+1))
        
    if answer != 'KAKTUS':
        break
    
print(answer)