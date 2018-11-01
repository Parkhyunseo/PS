N, M = map(int, input().split())
grid = []
homes = []
chickens = []
distances = []

def distance(start, end):
    return abs(start[0]-end[0]) + abs(start[1]-end[1])

for y in range(N):
    line = list(map(int, input().split()))
    for x in range(N):
        if line[x] == 1:
            homes.append((x, y))
        elif line[x] == 2:
            chickens.append((x, y))
            distances.append([0, (x, y)])
    grid.append(line)

for h in range(len(homes)):
    for c in range(len(chickens)):
        distances[c][0] += distance(homes[h], chickens[c])

distances.sort(key=lambda x:x[0])
s = 0

for h in range(len(homes)):
    minimum = 200000000
    for i in range(M):
        minimum = min(minimum, distance(homes[h], distances[i][1]))
    s += minimum

print(s)
"""    
def bfs(start):
    q = Queue()
    visit = [ [ False for _ in range(N)] for _ in range(N)] 
    q.put(start)
    
    find_y = -1
    find_x = -1
    
    while q.qsize() > 0 and find_y == -1:
        cur = q.get()
        visit[cur[1]][cur[0]] = True
        for d in direction:
            nx = cur[0] + d[0]
            ny = cur[1] + d[1]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visit[ny][nx]:
                continue
            
            if grid[ny][nx] == 2:
                find_y = ny
                find_x = nx
                break
            
            q.put((nx, ny))

    return abs(start[0]-find_x) + abs(start[1]-find_y)
    
while len(homes) > 0:
    home = homes.pop()
    bfs(home)
    
dist = reduce(lambda x,y : x+y, distances)
dist.sort()

s = 0
for i in range(M):
    s += distances[i]
    
print(s)
"""    
