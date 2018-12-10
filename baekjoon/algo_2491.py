N=int(input())
A = [ int(x) for x in input().split() ]
up_count = 1
down_count = 1
up_len = 0
down_len = 0
for i in range(1, N):
    if A[i] > A[i-1]:
        up_count += 1
        up_len = max(up_len, up_count)
        down_count = 1
    elif A[i] < A[i-1]:
        down_count += 1
        down_len = max(down_len, down_count)
        up_count = 1
    else:
        up_count += 1
        down_count += 1
        up_len = max(up_len, up_count)
        down_len = max(down_len, down_count)
        
if len(A)==1:
    print(1)
else:
    print(max(up_len, down_len))