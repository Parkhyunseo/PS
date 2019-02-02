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

N = int(stdin.readline())

vectors = []
for i in range(N):
    x, y = map(int, stdin.readline().split())
    vectors.append(Vector2D(x, y))

vectors.append(vectors[0])

result = 0
for i in range(N):
    result += (vectors[i].x*vectors[i+1].y - vectors[i+1].x*vectors[i].y)/2 
    
print(abs(result))