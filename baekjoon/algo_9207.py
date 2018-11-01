T = int(input())
direction = [(0,1), (0,-1), (1,0), (-1,0)]

for t in range(T):
    grid = input().split()
    
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "o":
            move_pin((x, y))
            
def move_pin(c):
    for d in direction:
        nx = c[0] + d[0]
        ny = c[1] + d[1]
        
        if ny >= len(grid) or ny < 0 or nx >= len(grid[0]) or nx < 0:
            continue
        
        if grid[ny][nx] == "o":
            move_pin((nx, ny))
        
        
            
