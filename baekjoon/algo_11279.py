from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline())
li = []

for i in range(N):
    get = int(stdin.readline())
    if get == 0:
        if len(li) > 0:
            print(-heappop(li))
        else:
            print(0)
    else:
        heappush(li, -get)