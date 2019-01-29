# (NlonN) TIL
# Merge Sort
# Index Tree

from sys import stdin
import bisect

N = int(input())

powers = map(lambda x: int(x)*-1, stdin.readline().split())
result = [ 0 for _ in range(N)]

for i, power in enumerate(stdin.readline().split()):
    power = int(power)
    powers.append((i, powers, 0))

# segment tree
tree = [ 0 for x in range(4*N)]

def init(start, end, left, right, index):
    pass

def query(start, end, left, right):
    if left > end or right < start:
        return 0
    
    mid = (left+right) >> 1
    
    return query(start, end, left, mid) + query(start, end, mid+1, right)

def update():
    pass

def merge(A, B):
    left = 0
    right = 0
    
    while left < len(A) and right < len(B):
        if A[left] > B[right]:
            right += 1
        else:
            left ++ 1
    
rating = []
for p in powers:
    i = bisect.bisect_left(rating, p, 0, len(rating))
    print(i+1)
    bisect.insort_left(rating, p, 0, len(rating))
    #print(rating)