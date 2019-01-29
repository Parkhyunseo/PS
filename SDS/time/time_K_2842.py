from sys import stdin

N = int(stdin.readline())

directions = [ (0, 1), (1, 1), (-1, 1), (-1, 0), (1, 0), (0, -1), (1, -1), (-1, -1)]

grid = []
stamina = [ [] for _ in range(N)]
stamina_set = set()

sx, sy = 0, 0
post_office_count = 0

for i in range(N):
    line = list(stdin.readline())
    for j in range(N):
        if line[j] == 'P':
            sx, sy = j, i
        elif line[j] == 'K':
            post_office_count += 1
    grid.append(line)
    
for i in range(N):
    for x in input().split():
        x = int(x)
        stamina[i].append(x)
        stamina_set.add(x)

stamina_set = sorted(list(stamina_set))
        
def dfs(x, y, left, right):
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
        
    if visited[y][x]:
        return 0
    
    if stamina[y][x] < left or stamina[y][x] > right:
        return 0
    
    visited[y][x] = True
    
    total = 0
    
    if grid[y][x] == 'K':
        total += 1
    
    for d in directions:
        nx = x + d[0]
        ny = y + d[1]
        total += dfs(nx, ny, left, right)
        
    return total
        
ans = 1000000
left = 0

for right in range(len(stamina_set)):
    while left <= right:
        visited = [ [ False for _ in range(N)] for _ in range(N)]
        count = dfs(sx, sy, stamina_set[left], stamina_set[right])
        
        if count != post_office_count:
            break
        
        ans = min(ans, stamina_set[right]-stamina_set[left])
        
        left += 1
        
print(ans)
    

    
    

