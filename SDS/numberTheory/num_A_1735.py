A,B = map(int, input().split())
C,D = map(int, input().split())

def gdc(a, b):
    if a < b:
        a, b = b ,a
    return a if b == 0 else gdc(b, a%b)

up = A*D + B*C
down = B*D
G = gdc(up,down)
print(up//G , down//G)