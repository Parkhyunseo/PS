from sys import stdin
from collections import namedtuple

N = int(stdin.readline())

Line2D = namedtuple('Line2D', ['v1','v2'])
Vector2D = namedtuple('Vector2D', ['x', 'y'])

def ccw(p1, p2, p3):
    temp = p1.x*p2.y + p2.x*p3.y + p3.x*p1.y
    temp = temp - (p1.y*p2.x + p2.y*p3.x + p3.y*p1.x)
    
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0

def is_cross(l1, l2):
    # l1과 l2의 v1 l1과 l2의 v2의 부호가 서로다른가. 
    # l2과 l1의 v1 l2과 l1의 v2의 부호가 서로다른가.
    # 만약 모두 0이라면
    #   y값이 모두 같다면 y범위 안에 포함되는지
    #   x값이 모두 같다면 x범위 안에 포함되는지
    
    cross = False
    
    ccw1 = ccw(l1.v1, l1.v2, l2.v1)
    ccw2 = ccw(l1.v1, l1.v2, l2.v2)
    ccw3 = ccw(l2.v1, l2.v2, l1.v1)
    ccw4 = ccw(l2.v1, l2.v2, l1.v2)
    
    if ccw1 * ccw2 <= 0:
        if ccw3 * ccw4 <= 0:
            cross = True
            if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
                mn = min(l1.v1.x, l1.v2.x, l2.v1.x, l2.v2.x)
                mx = max(l1.v1.x, l1.v2.x, l2.v1.x, l2.v2.x)
                if mn != mx: # x좌표가 모두 같지 않다면
                    l1_x_mn = min(l1.v1.x, l1.v2.x)
                    l1_x_mx = max(l1.v1.x, l1.v2.x)
                    
                    l2_x_mn = min(l2.v1.x, l2.v2.x)
                    l2_x_mx = max(l2.v1.x, l2.v2.x)
                    
                    if l1_x_mx < l2_x_mn or l2_x_mx < l1_x_mn:
                        cross = False
                else:
                    l1_y_mn = min(l1.v1.y, l1.v2.y)
                    l1_y_mx = max(l1.v1.y, l1.v2.y)
                    
                    l2_y_mn = min(l2.v1.y, l2.v2.y)
                    l2_y_mx = max(l2.v1.y, l2.v2.y)
                    
                    if l1_y_mx < l2_y_mn or l2_y_mx < l1_y_mn:
                        cross = False
                
    return cross

def find(v):
    if v == parent[v]:
        return v
        
    parent[v] = find(parent[v])
    return parent[v]
    
def merge(v, u):
    u = find(u)
    v = find(v)
    
    if u == v:
        return
    
    if rank[u] > rank[v]:
        u, v = v, u
        
    parent[u] = v
    rank[v] += rank[u]
    
    if rank[u] == rank[v]:
        rank[v] += 1
        
parent = [ i for i in range(3001)]
rank = [ 1 for _ in range(3001) ]

lines = []

for i in range(N):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    lines.append(Line2D(Vector2D(x1,y1), Vector2D(x2,y2)))
    
for i in range(N-1):
    for j in range(i+1, N):
        l1 = lines[i]
        l2 = lines[j]
        
        if is_cross(l1, l2):
            #print('is cross', i, j)
            
            merge(i, j)

#print(parent)
#print(rank)
        
group_count = 0
rank_max = 0
for i in range(N):
    if parent[i] == i:
        group_count += 1
    rank_max = max(rank_max, rank[i])
    
print(group_count)
print(rank_max)
        
            
    
