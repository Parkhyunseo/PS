T=int(input())
dp = [ -1 for _ in range(68) ]
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4 

def koong(n):
    if dp[n] != -1:
        return dp[n]
    
    if n < 4:
        return dp[n]
        
    dp[n] = koong(n-1) + koong(n-2) + koong(n-3)+ koong(n-4)
    return dp[n]
    

for t in range(T):
    N = int(input())
    print(koong(N))