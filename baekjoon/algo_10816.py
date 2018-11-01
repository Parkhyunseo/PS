import bisect

N = input()
A = map(int, raw_input().split())
M = input()
B = map(int, raw_input().split())

A.sort()
result = []

for m in xrange(M):
    found = bisect.bisect_left(A, B[m])
    
    count = 0
    if found == N:
        result.append(0)
        continue
    
    if A[found] == B[m]:
        right_found = bisect.bisect_right(A, B[m])
        count = right_found - found
            
    result.append(count)
    
print ' '.join([str(result[x]) for x in xrange(M)])