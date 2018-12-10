from queue import Queue
F,S,G,U,D = map(int, input().split())
visited = [ False for _ in range(F+1)]

def elevate(s):
    q = Queue()
    q.put((s,0))
    result = -1
    while q.qsize() > 0:
        item = q.get()
        here =item[0]
        count = item[1]
        
        if here == G:
            return count
        
        if here+U <= F:
            if not visited[here+U]:
                q.put((here+U, count+1))
                visited[here+U] = True
                
        if here-D > 0:
            if not visited[here-D]:
                q.put((here-D, count+1))
                visited[here-D] = True
            
    return "use the stairs"
    
print(elevate(S))    