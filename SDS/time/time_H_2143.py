# 자연수가아니라 정수
import bisect

T = int(input())
N = int(input())

A = [ int(x) for x in input().split()]
A_sum = []
for i in range(N):
    if i == 0:
        A_sum.append(A[i])
    else:
        A_sum.append(A_sum[-1] + A[i])
        
M = int(input())
B = [ int(x) for x in input().split()]
B_sum = []
for i in range(M):
    if i == 0:
        B_sum.append(B[i])
    else:
        B_sum.append(B_sum[-1] + B[i])

sub = []
for i in range(M):
    for j in range(i, M):
        sub.append(B_sum[j] - B_sum[i] + B[i])

sub.sort()
print(sub)

left = 0
right = 0
total = 0

count = 0

for left in range(N):
    for right in range(left, N):
        find = A_sum[right]-A_sum[left]+A[left]
        lo = bisect.bisect_left(sub, T-find)
        hi = bisect.bisect_right(sub, T-find)
    
        if lo < len(sub):
            if sub[lo] + find== T:
                print(left, right)
                count += hi - lo
"""
while True:
    if right < N:
        if total >= T:
            total -= A[left]
            left += 1
        elif right == N:
            break
        else:
            total += A[right]
            right += 1
    else:
        if left >= right:
            break
        
        total -= A[left]
        left += 1
    
    lo = bisect.bisect_left(sub, T-total)
    hi = bisect.bisect_right(sub, T-total)
    
    if lo < len(sub):
        if sub[lo] + total== T:
            print(left, right)
            count += hi - lo
"""         
print(count)
    