N, M = map(int, input().split())

houses = []
for i in range(N):
    houses.append(int(input()))

houses.sort()

ans = 0

left = 1
right = houses[-1] - houses[0]

while left <= right:
    mid = (left + right) >> 1
    
    #print(left, mid, right)
    
    before = houses[0]
    count = 1
    
    for i in range(1, N):
        if houses[i] >= before + mid:
            count += 1
            before = houses[i]
    
    if count < M: # 차이가 너무 크면
        right = mid - 1
    else:
        ans = mid
        left = mid + 1

print(ans)