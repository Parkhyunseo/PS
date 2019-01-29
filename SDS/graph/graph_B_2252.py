N, M = map(int ,input().split())

graph = [ [] for _ in range(N+1)]
indegree_count = [ 0 for _ in range(N+1)]
q = []
result = []

for i in range(M):
    front, behind = map(int, input().split())
    
    graph[front].append(behind)
    indegree_count[behind] +=1

for i in range(1, N+1):    
    if indegree_count[i] == 0:
        q.append(i)
        
while len(q) > 0:
    front = q.pop(0)
    
    for behind in graph[front]:
        indegree_count[behind] -= 1
        
        if indegree_count[behind] == 0:
            q.append(behind)
            
    result.append(front)
    
print(' '.join([str(x) for x in result]))
    

    