from sys import stdin 
from collections import namedtuple
from math import atan2

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

def get_convex_hull(points, N):
    stack = [0]
    
    point = 1 
    while point < N: # 0 ~ N-1
        while len(stack) >= 2:
            second = stack.pop()
            first = stack[-1]
            
            cw = ccw(points[first], points[second], points[point])
            
            if cw > 0:
                stack.append(second)
                break

        stack.append(point)
        point+= 1
    return stack
    
def find(convex_hull):
    a, b = convex_hull[0], convex_hull[1]
    #convex_hull_circle = convex_hull + convex_hull[:len(convex_hull)+1]
    
    max_distance = -1
    
    p = 1
    third = points[convex_hull[p]]
    fouth = points[convex_hull[p+1]]
    for i in range(len(convex_hull)):
        first = points[convex_hull[i]]
        second = points[convex_hull[(i+1)%len(convex_hull)]]
        
        while ccw(first, second, fouth) > 0:
            # 문제없다. 다음 점으로
            p = (p + 1) % len(convex_hull)
                    
            # next_p는 다음 점인데 평행이동된 점
            third = points[convex_hull[p]] # 정답이 될 점
            
            # 다음점 평행이동 값 구함
            diff = Vector2D(third.x - second.x, third.y - second.y)
            
            fouth = points[convex_hull[(p+1)% len(convex_hull)]] # 다음점 대입하고
            fouth = Vector2D(fouth.x-diff.x, fouth.y-diff.y) # 평행이동
            
            if points[convex_hull[p]] == first:
                break

        f_p_distance = get_euclidean_distance(first, third)
        f_s_distance = get_euclidean_distance(first, second)
        s_p_distance = get_euclidean_distance(second, third)

        if f_p_distance > max_distance:
            max_distance = f_p_distance
            a, b = first, third
            
        if f_s_distance > max_distance:
            max_distance = f_s_distance
            a, b = first, second
            
        if s_p_distance > max_distance:
            max_distance = s_p_distance
            a, b = second, third

    return (a, b)

def get_euclidean_distance(a, b):
    return (a.x - b.x)**2 + (a.y - b.y)**2

for t in range(T):
    N = int(stdin.readline())
    
    points = []
    for i in range(N):
        x, y = map(int, stdin.readline().split())
        points.append(Vector2D(x, y))
        
    points.sort(key=lambda vector: (vector.y, vector.x))
    start = points[0]
    ps = sorted(points[1:], key=lambda vector: atan2(vector.y-start.y, vector.x-start.x))
    points = [start] + ps
    
    convex_hull = get_convex_hull(points, N)
    
    a, b = find(convex_hull)
    print(a.x, a.y, b.x , b.y )
