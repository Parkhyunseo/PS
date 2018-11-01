"""N = int(input())
A = list(map(int, input().split()))
B = [ -1 for _ in range(N)]
count = 0

for i in range(1, N+1):
    A[i-1] = (A[i-1] - i, i-1)
    B[i-1] = A[i-1]

print(A)
A.sort(key=lambda x: abs(x[0]))

for a in A:
    val, ix = a
    
    for 
    if B[ix + val] == False:
        count += 1
        B[ix + val] = True
        
print(B)
print(count)
"""     
    
import bisect

N = int(input())
A = list(map(int, input().split()))
B = [A[0]]

for i in range(1, N):
    if B[-1] < A[i]:
        B.append(A[i])
    else:
        x = bisect.bisect_left(B, A[i], 0, len(B)-1)
        B[x] = A[i]
    print(B)
