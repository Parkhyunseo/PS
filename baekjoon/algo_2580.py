COL = 9
ROW = 9
grid = [ [] for _ in range(ROW) ] 
emptys = []
end = False

for i in range(ROW):
    line = input().split()
    for j in range(COL):
        if line[j] == '0':
            emptys.append((j, i))    
        grid[i].append(int(line[j]))
            
def possible(num ,x, y):
    for i in range(ROW):
        if grid[i][x] == num or grid[y][i] == num:
            return False
    
    sx = x//3*3
    sy = y//3*3
    for i in range(sy, sy+3):
        for j in range(sx, sx+3):
            if grid[i][j] == num:
                return False
                
    return True
    
def dfs(here):
    global end
    stop = True
    
    for i in range(COL):
        for j in range(ROW):
            if grid[i][j] == 0:
               stop = False
               break
        if not stop:
            break
    
    if stop:
        for i in range(ROW):
            print(' '.join([ str(x) for x in grid[i]]))    
        return
    
    x, y = emptys[here]
    
    for i in range(1, 10):
        if possible(i, x, y):
            grid[y][x] = i
            dfs(here+1)
            grid[y][x] = 0
    
        
dfs(0)