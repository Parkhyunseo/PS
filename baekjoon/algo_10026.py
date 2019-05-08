import sys
sys.setrecursionlimit(10000)
N = int(input())

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

image = []
visited = [ [ False for _ in range(N) ] for _ in range(N)]

normal = 0
abnormal = 0

def flow(cur, color, amblyopia):
    visited[cur[1]][cur[0]] = True
    
    for d in directions:
        nx = cur[0] + d[0]
        ny = cur[1] + d[1]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        
        if visited[ny][nx]:
            continue
    
        if image[ny][nx] == color:
            flow((nx, ny), image[ny][nx], amblyopia)
        elif amblyopia and ( ( image[ny][nx] == 'G' and color == 'R') or ( image[ny][nx] == 'R' and color == 'G') ):
            flow((nx, ny), image[ny][nx], amblyopia)
        
for i in range(N):
    image.append(list(input()))
    
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
    
        flow((j, i), image[i][j], False)
        normal += 1

visited = [ [ False for _ in range(N) ] for _ in range(N)]
        
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        
        flow((j, i), image[i][j], True)
        abnormal += 1
        
print(normal, abnormal)
            