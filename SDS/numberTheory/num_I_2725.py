def gcd(a, b):
    if a < b:
        a, b = b, a
        
    while b != 0:
        a, b = b, (a % b)
    return a

T = int(input())

ans = [ 0 for _ in range(1001)]
ans[0] = 0
ans[1] = 2

for i in range(2, 1001):
    count = 0
    for j in range(1, i+1):
        if gcd(j, i) == 1:
            count += 1
    ans[i] = ans[i-1] + count

for t in range(T):
    N = int(input())
    
    print(ans[N]*2 + -1)
                
            