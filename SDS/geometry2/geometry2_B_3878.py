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
            
            #print(point, points[first], points[second], points[point], cw)
            if cw > 0:
                stack.append(second)
                break

        stack.append(point)
        point+= 1
    return stack
    
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
    
def is_contain():
    pass

N, M = map(int, stdin.readline().split())

white = []
black = []

for i in range(N):
    x, y = map(int, stdin.readline().split())
    white.append(Vector2D(x, y))

white.sort(key=lambda vector: (vector.y, vector.x))
start = points[0]
white = sorted(white[1:], key=lambda vector: atan2(vector.y-start.y, vector.x-start.x))

white_convex_hull = get_convex_hull([start] + white, N)

for i in range(M):
    x, y = map(int, stdin.readline().split())
    black.append(Vector2D(x, y))

black.sort(key=lambda vector: (vector.y, vector.x))
start = points[0]
black = sorted(black[1:], key=lambda vector: atan2(vector.y-start.y, vector.x-start.x))

black_convex_hull = get_convex_hull([start] + black, M)

p = 0
white_lines = []
while p < len(white_convex_hull) - 1:
    white_lines.append(Line2D(white[white_convex_hull[p])], white[white_convex_hull[p+1])])
    
p = 0
black_lines = []

# 교차 확인 코드


# 검안 흰
# 흰안 검 
# 2번 체크
# 내부 확인 코드

print(len(convex_hull))