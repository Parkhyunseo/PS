from queue import Queue

N, K = map(int, input().split())
visited = [ False for _ in range(100001)]
values = [-1, 1, 0]
result = 100001
count = 0

def bfs(s):
    global result
    
    q = Queue()
    q.put((s, 0))
    visited[s] = True
    
    while q.qsize() > 0:
        item = q.get()
        p, c = item[0], item[1]
        
        visited[p] = True
        
        if result < c:
            continue
        
        if p == K:
            result = min(result, c)
            continue
            #return c
        
        for i in values:
            count = c
            if i==0:
                np = p * 2
            else:
                np = p + i;
                count += 1
            
            if np >= 0 and np <= 100000:
                if not visited[np]:
                 q.put((np, count))
                 
bfs(N)    
print(result)
    