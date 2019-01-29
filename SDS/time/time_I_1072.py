import sys

X, Y = map(int, input().split())
    
start = 0
end = 1000000000
    
target = int(Y * 100 / X)
    
if target >= 99:
    print(-1)
    sys.exit()
    
ans = 0
    
while end >= start:
    mid = (start + end) >> 1
    #print(mid, int((Y+mid)*100/(X+mid)), target)
        
    if int((Y+mid)*100/(X+mid)) > target:
        end = mid - 1
    else:
        start = mid + 1
        ans = start
        
print(ans)