import bisect 

N = input()
A = map(int, raw_input().split())
M = input()
to_look_for = map(int, raw_input().split())

A.sort()

for i in xrange(M):
    found = bisect.bisect_right(A, to_look_for[i])

    if A[found-1] == to_look_for[i]:
        print 1
    else:
        print 0
