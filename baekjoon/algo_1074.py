N, C, R = map(int, input().split())
count = 0

def divide(n, lt, rb, r, c):
    global count
    
    if n == 0:
        return
    
    addition = 2**(n-1) * 2**(n-1)  
    
    lts = [(lt[0], lt[1]), (lt[0] + 2**(n-1), lt[1]), (lt[0], lt[1]+ 2**(n-1))]
    rbs = [(rb[0]/2, rb[1]/2), (rb[0]/2 + 2**(n-1), rb[1]/2), (rb[0]/2, rb[1]/2 + 2**(n-1))]
    
    for i in range(3):
        if r >= lts[i][0] and r <= rbs[i][0] and c >= lts[i][1] and c <=  rbs[i][1]:
            divide(n-1, lts[i], rbs[i], r,c)
            return
        else:
            count += addition
        
    divide(n-1, (lt[0] + 2**(n-1), lt[1] + 2**(n-1)), (rb[0]/2 + 2**(n-1), rb[1]/2 + 2**(n-1)), r,c)

if N == 1:
    if R == 0 and C == 0:
        count = 1
    elif C == 0 and R == 1:
        count = 2
    elif C == 1 and R == 0:
        count = 3
    elif R == 1 and C == 1:
        count = 4
else:
    divide(N, (0,0), (2**N, 2**N), R+1, C+1)

print(count)