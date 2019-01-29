def solution(l, v):
    answer = 0

    left = 0
    right = 1000000000

    v.sort()
    
    while right > left:
        end = 0
        
        mid = (left + right) // 2
        possible = True
        
        for i in range(len(v)):
            if i == 0:
                if v[i] - mid > 0:
                    possible = False
                    break
                else:
                    end = v[i] + mid
                    continue
                    
            if v[i] - mid > end:
                possible = False
                break
            
            end = v[i] + mid
            
        if end < l:
            possible = False
            
        if possible:
            right = mid
        else:
            left = mid + 1
            
    answer = right + 1
    
    return answer
    
N = int(input())
M = [ int(x) for x in input().split() ]
print(solution(N,M))