N = int(input())
requires = [ int(x) for x in input().split()]
total = int(input())

if total >= sum(requires):
    print(max(requires))
else:
    #requires.sort()
    
    left = 0
    right = max(requires)
    while left < right:
        mid = (left + right) >> 1
        
        sums = 0
        for i in range(N):
            if requires[i] <= mid:
                sums += requires[i]
            else:
                sums += mid
                
        if sums <= total:
            left = mid + 1
        else:
            right = mid

    print(left-1)
                
        