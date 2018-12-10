T = int(input())

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def dot(x1, y1, x2, y2):
    return x1*x2+y1*y2

for t in range(T):
    points = []
    flag = False
    distances = [ [ 2000001 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        x, y = map(int, input().split())
        points.append((x, y))
        
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            distances[i][j] = distance(points[i][0], points[i][1], points[j][0], points[j][1])
    
    for i in range(4):
        li = sorted(distances[i])
        d1 = distance(points[i][0], points[i][1], li[0][0], li[0][1])
        d2 = distance(points[i][0], points[i][1], li[1][0], li[1][1])
        
        if d1 != d2:
            flag = True
            break
        
    if flag:
        print(0)
        continue
    else:
        for i in range(4):
            li = sorted(distances[i])
            result = dot(li[0][0]-points[i][0], li[0][1]-points[i][1], li[1][0]-points[i][0], li[1][1]-points[i][0])
            
            if result != 0:
                flag = True
                break
            
        if flag:
            print(0)
        else:
            print(1)
            
            