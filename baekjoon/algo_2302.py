N = int(input())
M = int(input())

dp = [ -1 for _ in range(N+1)]

def fibo(n):
    if dp[n] != -1:
        return dp[n]
        
    if n <= 1:
        return 1
    
    dp[n] = fibo(n-1) + fibo(n-2) 
    return dp[n]
    
result = 1

before_vip = 0
for m in range(M):
    vip = int(input())
    result *= fibo(vip-before_vip-1)
    before_vip = vip
    
if N - before_vip > 0 :
    result *= fibo(N - before_vip)
    
print(result)

    
# f[1] = 2
# f[2] = 3
# f[3] = 4