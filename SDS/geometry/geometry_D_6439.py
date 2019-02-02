from sys import stdin
from collections import namedtuple

T = int(stdin.readline())

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
    
def is_contain(find):
    x_mn = lines[0].v1.x
    x_mx = lines[0].v1.x
    y_mn = lines[0].v1.y
    y_mx = lines[0].v1.y
    
    for line in lines:
        x_mn = min(x_mn, line.v1.x, line.v2.x)
        x_mx = max(x_mx, line.v1.x, line.v2.x)
        y_mn = min(y_mn, line.v1.y, line.v2.y)
        y_mx = max(y_mx, line.v1.y, line.v2.y)
        
    if find.v1.x >= x_mn and find.v1.x <= x_mx and\
        find.v2.x >= x_mn and find.v2.x <= x_mx:
        if find.v1.y >= y_mn and find.v1.y <= y_mx and\
                find.v2.y >= y_mn and find.v2.y <= y_mx:
            return True
    
    return False
            

for t in range(T):
    lines = []

    result = 'F'

    xs, ys, xe, ye, x1, y1, x2, y2, = map(int, stdin.readline().split())
    lines.append(Line2D(Vector2D(x1,y1), Vector2D(x2,y1)))
    lines.append(Line2D(Vector2D(x2,y1), Vector2D(x2,y2)))
    lines.append(Line2D(Vector2D(x2,y2), Vector2D(x1,y2)))
    lines.append(Line2D(Vector2D(x1,y2), Vector2D(x1,y1)))
    
    find = Line2D(Vector2D(xs, ys), Vector2D(xe, ye))
    
    for i in range(3):
        for j in range(i+1, 4):
            line = lines[i]
            
            if is_cross(line, find):
                result = 'T'
                
            if is_contain(find):
                result = 'T'
    
    print(result)
            
    
