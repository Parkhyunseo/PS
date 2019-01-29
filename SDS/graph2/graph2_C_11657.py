from sys import stdin

V, E = map(int, stdin.readline().split())
INF = (V-1) * 10000 * 2 + 1

dist = [INF] * (V+1)
graph = [  ]

class Edge():
    def __init__(self, f, t, w):
        self.f = f
        self.t = t
        self.w = w
    
    def get(self):
        return (self.f, self.t, self.w)

for e in range(E):
    f ,t , w = map(int, stdin.readline().split())
    graph.append(Edge(f, t, w))
    
dist[1] = 0
for v in range(V-1):
    for e in range(E):
        f, t, w =  graph[e].get()
        
        if dist[f] != INF:
            if dist[t] > dist[f] + w:
                dist[t] = dist[f] + w

have_circle = 0
for e in range(E):
    f, t, w =  graph[e].get()
    
    if dist[t] != INF:
        if dist[t] > dist[f] + w:
            have_circle = -1
            break
    
if have_circle == -1:
    print(-1)
else:
    for i in range(2, V+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
        

        
        
        
    