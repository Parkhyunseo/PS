# (NlonN) TIL
# Merge Sort
# Index Tree

from sys import stdin
import bisect

N = int(input())

powers = map(lambda x: int(x)*-1, stdin.readline().split())
match = dict()
result = [ 0 for _ in range(N)]

for i, power in enumerate(stdin.readline().split()):
    power = int(power)
    powers.append((i, power, 0))
    match[i] = power
    
powers.sort(key=lambda x:x[0])

order = [match[0]]
result = [1]

for i in range(1, N):
    man = match[i]
    
    if order[-1] < man:
        result.append(1)
    else:
        idx = bisect.bisect_left(result, man)
        bisect.insort_left(result, p)
        
        
        
