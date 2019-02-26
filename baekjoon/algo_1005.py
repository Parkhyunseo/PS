T = int(input())

def bfs(here):
    if memoization[here] != -1:
        return memoization[here]
        
    result = 0
    
    for there in graph[here]:
        result = max(result, bfs(there))
        
    memoization[here] = result + time[here]
    return memoization[here]

for t in range(T):
    N, K = map(int, input().split())
    
    graph = [ [] for _ in range(N+1)]
    memoization = [ -1 for _ in range(N+1)]
    time = [ 0 ]
    
    for x in input().split():
        time.append(int(x))
        
    for i in range(K):
        f, t = map(int, input().split())
        graph[t].append(f)
        
    find = int(input())
    print(bfs(find))
        

    
    