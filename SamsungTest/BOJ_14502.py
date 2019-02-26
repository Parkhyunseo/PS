N, M = map(int, input().split())

grid = [ [ 0 for _ in range(M)] for _ in range(N)]
directions = [ (0, 1), (0, -1), (1, 0), (-1, 0)]
infections = []

for i in range(N):
    line = input().split()
    for j in range(M):
        grid[i][j] = line[j]
        if line[j] == '2':
            infections.append((j, i))
   
# 감염     
def infect():
    q = [ pos for pos in infections ]

    while len(q) > 0:
        pos = q.pop(0)
        
        for d in directions:
            nx = pos[0] + d[0]
            ny = pos[1] + d[1]
            
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            
            if grid[ny][nx] == '0':
                grid[ny][nx] = '3'
                q.append((nx, ny))

def solve():
    global result 
    
    infect()
    
    count = 0
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '0':
                count += 1
                
            if grid[i][j] == '3': # 정화
                grid[i][j] = '0'
    
    result = max(result, count)
        
#벽을 새운다
def build():
    for i in range(N*M-2):
        for j in range(i+1, N*M-1):
            for k in range(j+1, N*M):
                ix, iy = i % M, i // M
                jx, jy = j % M, j // M
                kx, ky = k % M, k // M
                
                if grid[iy][ix] == '0' and grid[jy][jx] == '0' and grid[ky][kx] == '0':
                    grid[iy][ix] = '1'
                    grid[jy][jx] = '1'
                    grid[ky][kx] = '1'
                    solve()
                    grid[iy][ix] = '0'
                    grid[jy][jx] = '0'
                    grid[ky][kx] = '0'
                    
result = 0
build()
print(result)
