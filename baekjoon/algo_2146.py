from sys import stdin

N = int(stdin.readline())
dirs = [ (0, 1), (0, -1), (1, 0), (-1, 0)]
world = []

for i in range(N):
    world.append([int(x) for x in stdin.readline().split()])
    
def mark_area(start:tuple, sign:int) -> None:
    q = [start]
    world[start[1]][start[0]] = sign
    
    while len(q) > 0:
        here = q.pop(0)
        
        for d in dirs:
            nx, ny = here[0] + d[0], here[1] + d[1]
        
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if world[ny][nx] != 1:
                continue
            
            world[ny][nx] = sign
            q.append((nx, ny))
            
def find_min_dist(start: tuple, sign:int)-> int:
    q = [start]
    world[start[1]][start[0]] = sign
    
    while len(q) > 0:
        here = q.pop(0)
        
        for d in dirs:
            nx, ny = here[0] + d[0], here[1] + d[1]
        
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if world[ny][nx] == sign:
                q.append((nx, ny, 0))
            elif world[ny][nx] == 0:
                if world[here[1]][here[0]]:
                    q.append((nx, ny, 1))
                else:
                    q.append((nx, ny, here[3]+1))
            else:
                return here[3]
                
c_sign = 2
for i in range(N):
    for j in range(N):
        if world[i][j] == 1:
            mark_area((j, i), c_sign)
            c_sign += 1
            
for i in range(N):
    print(world[i])

for i in range(2, c_sign):
    
    