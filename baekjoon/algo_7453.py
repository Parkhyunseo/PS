# 시간초과 => c++풀 것
from bisect import bisect_left, bisect_right
from sys import stdin

N = int(stdin.readline())
A, B, C, D = [], [], [], []
A_B = []
C_D = []
count = 0

for i in range(N):
    a, b, c, d = map(int, stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for i in range(N):
    for j in range(N):
        #A_BA[i]+B[j]
        C_D.append(C[i]+D[j])
        
#A_B.sort()
C_D.sort()

for i in range(N):
    for j in range(N):
        a = A[i] + B[j]
        lo = bisect_left(C_D, -a)
        hi = bisect_right(C_D, -a)
        
            
        if lo < len(C_D):
            if a + C_D[lo] == 0:
                #print(a, C_D[lo], lo, hi)
                count += hi - lo
            
print(count)