from sys import stdin

N, M = map(int, stdin.readline().split())
sheds = [ [] for _ in range(M) ]
b = [ -1 for _ in range(M)]
visit = []
    
def dfs(here: int) -> bool:
    if visit[here]:
        return False
    visit[here] = True
    
    for i in range(len(sheds[here])):
        there = sheds[here][i]
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
    
for i in range(N):
    shed = [ int(x)-1 for x in stdin.readline().split()]
    sheds[i] = (shed[1:])
    
result = bmatch()
print(result)