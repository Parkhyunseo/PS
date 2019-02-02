from sys import stdin
from collections import namedtuple

T = int(stdin.readline())

Line2D = namedtuple('Line2D', ['v1','v2'])
Vector2D = namedtuple('Vector2D', ['x', 'y'])

def dot(l1, l2):
    return (l1.v2.x-l1.v1.x)*(l2.v2.x-l2.v1.x) + (l1.v2.y-l1.v1.y)*(l2.v2.y-l2.v1.y)

def get_length(line):
    return ((line.v1.x - line.v2.x)**2 + (line.v1.y - line.v2.y)**2) #길이 비교니까 굳이 루트 x 

def get_center_point(line):
    return Vector2D((line.v1.x + line.v2.x)/2, (line.v1.y + line.v2.y)/2)

lines = []

# 1. 길이가 모두 같은가
# 2. 중점이 같다.

for t in range(T):
    vectors = []
    
    for n in range(4):
        x, y = map(int, stdin.readline().split())
        vectors.append(Vector2D(x, y))
    
    lines = []
    for i in range(3):
        for j in range(i+1, 4):
            p1 = vectors[i]
            p2 = vectors[j]
            
            lines.append(Line2D(p1, p2))
            
    lines.sort(key=lambda x: get_length(x), reverse=True)

    candidate_1 = lines[0]
    candidate_2 = lines[1]
    
    remain = [ get_length(line) for line in lines[2:]]
    if min(remain) != max(remain):
        print(0)
        continue
  
    if get_length(candidate_1) != get_length(candidate_2):
        print(0)
        continue
  
    if get_center_point(candidate_1) != get_center_point(candidate_2):
        print(0)
        continue
  
    print(1)
        
