import bisect

N, M = map(int, raw_input().split())
houses = []

for i in range(M):
    houses.append(input())

houses.sort()

#def solve(fm, to, count):
#    i = bisec.bisec(houses, (houses[fm] + houses[to]) / 2)
    
#solove(0, N-1)
    