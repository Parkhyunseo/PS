N = int(input())

graph = [ [] for _ in range(N+1)]
indegree_count = [ 0 for _ in range(N+1)]
times = [ 0 for _ in range(N+1)]
result = [ 0 for _ in range(N+1)]

q = []

for i in range(1, N+1):
    time, *prev = map(int, input().split())
    times[i] = time
    result[i] = time
    
    if len(prev) <= 1:
        continue
    
    prev = prev[:-1]
    
    for p in prev:
        graph[p].append(i)
        indegree_count[i] += 1

for i in range(1, N+1):    
    if indegree_count[i] == 0:
        q.append(i)

while len(q) > 0:
    front = q.pop(0)
    max_time = 0
    
    for behind in graph[front]:
        indegree_count[behind] -= 1
        
        result[behind] = max(result[behind], result[front] + times[behind])
        if indegree_count[behind] == 0:
            q.append(behind)
    
for r in result[1:]:
    print(r)
    

    