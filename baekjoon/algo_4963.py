direction = [ (0,1), (1,0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1,-1), (-1, 1)]
result = []

def dfs(pos):
    v[pos[1]][pos[0]] = 1
    
    for d in direction:
        next_x = pos[0]+d[0]
        next_y = pos[1]+d[1]
        
        if ( next_x < 0 ) or ( next_x >= W ) or ( next_y < 0 ) or ( next_y >= H ):
            continue
        
        if (land[next_y][next_x] == 1) and (v[next_y][next_x] == 0):
            dfs((next_x, next_y))

while True:
    # region input
    W, H = map(int, input().split())
    
    if ( W == 0 ) and ( H == 0) :
        break
        
    land = []
    v = [ [ 0 for _ in range(W) ] for _ in range(H)]
    count = 0
    
    for i in range(H):
        line = input()
        if len(line) > 1:
            land.append(list(map(int, line.split())))
        else:
            land.append([int(line)])
    # end region
    
    # region algorithm
    for y in range(H):
        for x in range(W):
            if (land[y][x] == 1) and (v[y][x] == 0):
                dfs((x, y))
                count += 1

    result.append(count)

for r in result:
    print(r)