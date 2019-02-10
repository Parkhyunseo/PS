from sys import stdin
R, C = map(int, input().split())

table = []
visited = [ False for _ in range(26)]
directions = [ (0,1), (1,0), (-1, 0), (0, -1)]

result = 0

for i in range(R):
    table.append(stdin.readline()[:-1])
    
def get_index(t: str) -> int:
    return ord(t) - ord('A')
    
def dfs(here:tuple, depth:int) -> None :
    global result
    
    result = max(depth, result)
    
    for d in directions:
        nx, ny = here[0] + d[0], here[1] + d[1]
        
        if nx < 0 or nx >= C or ny < 0 or ny >= R:
            continue
        
        ix = get_index(table[ny][nx])
        #print(table[ny][nx], ix, depth)
        if visited[ix]:
            continue
        
        visited[ix] = True
        dfs((nx, ny), depth+1)
        visited[ix] = False
        

visited[get_index(table[0][0])] = True    
dfs((0,0), 1)

print(result)