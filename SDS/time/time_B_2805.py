N, M = map(int, input().split())
height = sorted([int(x) for x in input().split()], reverse=True)
MAX = sum(height)

low = 0
high = height[0]
ans = 0
find = False

while low <= high:
    total = MAX
    mid = (low + high) >> 1
    
    for i in range(N):
        if height[i] >= mid:
            total -= mid
        else:
            total -= height[i]
    
    if total == M:
        ans = mid
        find = True
        
    if M < total:
        low = mid +1
    else:
        ans = mid
        high = mid - 1
        
if not find:
    ans = (low + high) >> 1
        
print(ans)
