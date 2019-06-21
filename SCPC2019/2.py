import math

T = int(input())

for t in range(T):
    R, S, E = map(int, input().split())
    
    N = int(input())
    
    distance = 0
    last_ri = S
    
    for i in range(N):
        li, ri, hi = map(int, input().split())
        
        distance += ri-li
        distance += max(2*(hi-R), 0)
        distance += li - last_ri - 2*R 
        if hi < R:
            distance += 2*math.pi*R*math.atan(R/R-hi)*2
        else:
            distance += math.pi*R
        last_ri = ri
        
    distance += E - last_ri - R
    distance += R
    
    print("Case #{0}".format(t+1))
    print(distance)