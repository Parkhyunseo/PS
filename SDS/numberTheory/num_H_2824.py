from functools import reduce
import sys
sys.setrecursionlimit(1000000000)

N = int(input())
l1 = map(int, input().split())
n1 = reduce(lambda x,y: x*y, l1)
M = int(input())
l2 = map(int, input().split())
n2 = reduce(lambda x,y: x*y, l2)

def gcd(a, b):
    if a < b:
        a, b = b, a
        
    return a if b == 0 else gcd(b, a%b)
    
result = str(gcd(n1, n2))

if len(result) > 10:
    print(result[-9:])
else:
    print(result)
