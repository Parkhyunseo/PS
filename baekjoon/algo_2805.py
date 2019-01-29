#O(NlogN)
#python은 느리다.
N, M = map(int, input().split())
heights = sorted([ int(x) for x in input().split()], reverse=True)
MAX = sum(heights)

start = 0
end = heights[0]
find = False
result = 0

while start <= end:
    mid = (start + end ) // 2
    #print("톱 높이 : " + str(mid))
    #print("벌목 시작할 최소 나무 높이 : " + str(heights[pos]))
    total = MAX
    
    for i in range(N):
        if heights[i] >= mid:
            total -= mid
        else:
            total -= heights[i]
    
    #print("총 얻은 목제 : " + str(total))
    if total == M:
        find = True
        result = mid
        break
    
    if M < total:
        start = mid + 1
    else:
        end = mid - 1
        
if not find:
    result = ( start + end ) >> 1
print(result)
    
