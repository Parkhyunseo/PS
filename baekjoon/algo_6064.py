T = int(input())

"""
M = 10, N = 12
diff = 
1 1
1 11
1 9
1 7
1 5
1 3
이 전날이 마지막 해
1 1

M = 12, N = 10
1 1
1 3
1 5
1 7
1 9
1 11
"""

# X를 N으로 나누었을 때 나머지가 y이고
# X를 M으로 나누었을 때 나머지가 x인 값
"""
def solve(M, N, x, y):
    find = False
    count = 1
    
    cx = 1
    cy = 1
    
    while not (M == cx and N == cy):
        cx += 1
        cy += 1
        
        if cx > M:
            cx = 1
        
        if cy > N:
            cy = 1
        
        count += 1
        
        if cx == x and cy == y:
            find = True
            break
        
    if not find:
        count = -1
        
    return count
"""

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)
    
def lcm(a, b):
    return a*b//gcd(a, b)

def solve(M, N ,x, y):
    count = x % (M+1)
    cy = x
    
    for i in range(N):
        ny = N if cy % N == 0 else cy % N
        
        if ny == y:
            break
        
        cy = ny + M
        count += M
        
    return count if lcm(max(M,N), min(M,N)) > count else -1

for t in range(T):
    M, N, x, y = map(int, input().split())
    print(solve(M, N, x, y))