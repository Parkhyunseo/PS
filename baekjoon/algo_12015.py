from sys import stdin
N = int(stdin.readline())
A = [ int(x) for x in stdin.readline().split()]
result = [A[0]]

def low_bound(start, end, find):
    while start < end:
        mid = (start + end) >> 1
        
        if find > result[mid]:
            start = mid + 1
        else:
            end = mid
  
    return end + 1

for i in range(N):
    if result[-1] < A[i]:
        result.append(A[i])
    else:
        idx = low_bound(0, len(result)-1, A[i])
        result[idx-1] = A[i]
        
print(len(result))