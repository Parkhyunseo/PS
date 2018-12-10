N = int(input())
dp = [ 0 for _ in range(N+1)]
dp[1] = 1

for i in range(1, N+1):
    for j in range(1, i):
        if i-j**2 >= 0:
            dp[i] =  dp[i-j**2] + 1
            #print(i, j)
        else:
            break
        
print(dp[N])