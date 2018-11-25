from queue import Queue

N, K = map(int, input().split())
visited = [ False for _ in range(100001)]
values = [-1, 1, 0]
traces = [-1 for _ in range(100001)]
result = 100001
count = 0

def bfs(s):
    q = Queue()
    q.put((s, 0))
    visited[s] = True
    
    while q.qsize() > 0:
        item = q.get()
        p, c = item[0], item[1]
        
        if p == K:
            return c
        
        for i in values:
            if i==0:
                np = p * 2
            else:
                np = p + i;
            
            if np >= 0 and np <= 100000:
                if not visited[np]:
                 q.put((np, c+1))
                 visited[np] = True
                 traces[np] = p
                 
c = bfs(N)
result = [K]
while K != N:
    result.append(traces[K])
    K = traces[K]
    
print(c)
print(' '.join([str(x) for x in reversed(result)]))
    