from sys import stdin

N, K = map(int, stdin.readline().split())
X, Y = [], []
count = 0
result = 0
edges = [ [] for _ in range(N)]
visit = []
b = [ -1 for _ in range(N) ]

def dfs(here: int) -> bool:
    if visit[here]:
        return False
    visit[here] = True
    
    for i in range(len(edges[here])):
        there = edges[here][i]
        if b[there] == -1 or dfs(b[there]):
            b[there] = here
            return True
            
    return False

def bmatch() -> int:
    global visit
    
    ret = 0
    for i in range(N):
        visit = [ False for _ in range(N)]
        if dfs(i):
            ret += 1
            
    return ret

for k in range(K):
    x, y = map(int, stdin.readline().split())
    edges[x-1].append(y-1)
    
ret = bmatch()
print(ret)
