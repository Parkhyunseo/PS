N, M = map(int, input().split())

castle = []
visit_row = [ False for _ in range(N) ]
visit_col = [ False for _ in range(M) ]

for i in range(N):
    castle.append(list(map(int, input().split())))
    
def dfs(x, y):
    if visit_row[y]:
        return
    
    if visit_col[x]:
        return
    
    visit_col[x] = True
    visit_row[y] = True
    
    for