N, S = map(int, input().split())
A =  [ int(x) for x in input().split() ]

left = 0
right = 0
total = 0

ans = N+1

while True:
    if total >= S:
        total -= A[left]
        left += 1
    elif right == N:
            break
    else:
        total += A[right]
        right += 1
    
    if total >= S:
        ans = min(ans, right-left)
    
if ans == N+1:
    print(0)
else:
    print(ans)