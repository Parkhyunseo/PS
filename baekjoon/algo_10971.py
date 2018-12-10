N = int(input())
visited = [ False for _ in range(N)]
W = []

result = 987654321

def tsp(here, cost, count, entry):
    if count == N:
        global result
        if W[here][entry] != 0:
            result = min(result, cost+W[here][entry])
        return
    
    if cost > result:
        return
    
    for there in range(N):
        if not visited[there] and W[here][there] != 0:
            visited[there] = True
            tsp(there, cost+W[here][there], count+1, entry)
            visited[there] = False

for i in range(N):
    line = [ int(x) for x in input().split()]
    W.append(line)

for i in range(N):
    visited[i] = True
    tsp(i, 0, 1, i)
    visited[i] = False
    
print(result)
    
    