from sys import stdin
from collections import namedtuple
from math import atan2

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

def get_convex_hull(points, N):
    stack = [0]
    
    point = 1 
    while point < N: # 0 ~ N-1
        while len(stack) >= 2:
            second = stack.pop()
            first = stack[-1]
            
            cw = ccw(points[first], points[second], points[point])
            
            #print(point, points[first], points[second], points[point], cw)
            if cw > 0:
                stack.append(second)
                break

        stack.append(point)
        point+= 1
    return stack
    

points = []
for i in range(N):
    x, y = map(int, stdin.readline().split())
    points.append(Vector2D(x, y))
    
points.sort(key=lambda vector: (vector.y, vector.x))
#print(points)
start = points[0]
# atan 정렬
ps = sorted(points[1:], key=lambda vector: atan2(vector.y-start.y, vector.x-start.x))

#print(start)
#print(ps)

convex_hull = get_convex_hull([start] + ps, N)

#print(convex_hull)
print(len(convex_hull))