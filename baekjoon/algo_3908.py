T = int(input())
primes = [ True for _ in range(1121)]
bag = []
dp = [ [ 0 for _ in range(16) ] for _ in range(1121)]
dp[0][0]=1 
primes[0] = False
primes[1] = False

def eratos():
    for i in range(2, int(1120**0.5)+1):
        if primes[i] == True:
            for j in range(i*i, 1121, i):
                primes[j] = False
    for i in range(2, 1121):
        if primes[i]:
            bag.append(i)
    
eratos()
for i in bag:
    for j in range(1120, i-1, -1):
        for k in range(1, 16):
            dp[j][k] += dp[j-i][k-1]
        
for t in range(T):
    N, K = map(int, input().split())
    print(dp[N][K])
    