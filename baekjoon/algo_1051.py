N, M = map(int, input().split())
table = []

for i in range(N):
    table.append(list(input()))
    
def find(start:tuple, sign:str) -> int:
    result = 1
    
    sx = start[0]
    sy = start[1]
    
    dist = min(N-sy-1, M-sx-1)
    
    for d in range(1, dist+1):
        s = set([sign, table[sy+d][sx], table[sy][sx+d], table[sy+d][sx+d]])
        
        if len(s) == 1:
            #print([sign, table[sy+d][sx], table[sy][sx+d], table[sy+d][sx+d]])
            result = d + 1
        
    return result
    
answer = 1

for i in range(N):
    for j in range(M):
        answer = max(answer, find((j, i), table[i][j]))
        
print(answer*answer)
        
        
    