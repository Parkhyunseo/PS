import bisect

N = input()
A = map(int, raw_input().split())
M = input()
B = map(int, raw_input().split())

A.sort()
result = []

for i in range(M):
    found = bisect.bisect_right(A, B[i])
    
    if A[found-1] == B[i]:
        result.append(1)
    else:
        result.append(0)
        
print ' '.join([str(x) for x in result])