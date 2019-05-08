N, M = map(int, input().split())
A = [ int(x) for x in input().split() ]

left = 0
right = 0
total = 0
result = 0

while True:
    if total >= M:
        total -= A[left]
        left += 1
    elif right == N:
        break
    else:
        total += A[right]
        right += 1
        
    if total == M:
        result += 1
    
print(result)
    
        
