from itertools import combinations
from fractions import gcd
T = int(input())
for t in range(T):
    N, *A = map(int, input().split())
    s=0
    for a in combinations(A, 2):
        s+=gcd(*a)
    print(s)