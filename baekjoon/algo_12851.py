from queue import Queue

N, K = map(int, input().split())
visited = [ False for _ in range(100001)]
values = [-1, 1, 0]
cnt = {}
result = 100001
count = 0

def bfs(s):
    global count
    global result
    
    q = Queue()
    q.put((s, 0))
    visited[s] = True
    
    while q.qsize() > 0:
        item = q.get()
        p, c = item[0], item[1]
        
        if c > result:
            return
        
        visited[p] = True
                
        if p == K:
            if c in cnt:
                cnt[c] += 1
            else:
                cnt[c] = 1
            result = min(result, c)
        
        for i in values:
            if i==0:
                np = p * 2
            else:
                np = p + i;
            
            if np >= 0 and np <= 100000:
                if not visited[np]:
                 q.put((np, c+1))

bfs(N)
print(result)
print(cnt[result])
    
        