from sys import stdin
from collections import namedtuple

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
        
x, y = map(int, stdin.readline().split())
p1 = Vector2D(x, y)
x, y = map(int, stdin.readline().split())
p2 = Vector2D(x, y)
x, y = map(int, stdin.readline().split())
p3 = Vector2D(x, y)
print(ccw(p1, p2, p3))