from sys import stdin

N, M = map(int, stdin.readline().split())
predcitions = [ [] for _ in range(N)]
b = [ -1 for _ in range(N)]
visit = []

def dfs(here: int) -> bool:
    if visit[here]:
        return False
    visit[here] = True
    
    for i in range(len(predcitions[here])):
        there = predcitions[here][i]
        if b[there] == -1 or dfs(b[there]):
            b[there] = here
            return True
            
    return False
    
def bmatch() -> int:
    global visit
    result = 0
    
    for i in range(N):
        visit = [ False for _ in range(N)]
        if dfs(i):
            result += 1
            
    return result
        
for _ in range(M):
    f, t = map(lambda x : int(x)-1, stdin.readline().split())
    predcitions[f].append(t)

result = bmatch()
print(result)
    
    
    