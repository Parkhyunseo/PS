N = int(input())

directions = [ (0, -1), (0, 1), (-1, 0), (1, 0)]
MAX_HEIGHT = 100

grid = []
result = 1

for n in range(N):
    grid.append([int(x) for x in input().split()])
    
def flood(pos:tuple, height:int):
    global visited
    
    q = []
    q.append(pos)
    visited[pos[1]][pos[0]] = True
    
    while len(q) > 0:
        here = q.pop(0)
        
        for d in directions:
            nx = here[0] + d[0]
            ny = here[1] + d[1]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if visited[ny][nx]:
                continue
            
            if grid[ny][nx] > height:
                continue
            
            visited[ny][nx] = True
            q.append((nx, ny))
            
def regionCount():
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                flood((j, i), 101)
                count += 1
                
    return count
    
for min_height in range(1, MAX_HEIGHT+1):
    visited = [ [ False for _ in range(N)] for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] <= min_height:
                flood((j, i), min_height)
            
    result = max(result, regionCount())
    
print(result)