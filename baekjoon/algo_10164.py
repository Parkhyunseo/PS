N, M, K = map(int, input().split())

def number_of_case(a, b):
    if b == -1:
        return 1
    
    #if a+1 == b:
    #    return 1
        
    if a == -1:
        a = 0
    
    sr = a // M
    sc = a % M
    
    er = b // M
    ec = b % M
   
    dp = [ [ 1 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i < sr or j < sc:
                dp[i][j] = 0
    
    for i in range(sr, er+1):
        #print(dp[i])
        for j in range(sc, ec+1):
            
            if i == sr or j == sc:
                continue
            
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
            
    return dp[er][ec]

r = number_of_case(0, K-1)
r *= number_of_case(K-1, N*M-1)

print(r)  