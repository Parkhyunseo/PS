T = int(input())

for t in range(T):
    K = int(input())
    dp = [ [ 0 for _ in range(K+1)] for _ in range(K+1)]
    dp2 = [ [ 0 for _ in range(K+1)] for _ in range(K+1)]
    files = [ 0 ]
    sums = [ 0 ]
    
    for f in input().split():
        f = int(f)
        files.append(f)
        sums.append(sums[-1] + f)
    
    for i in range(1, K+1):
        dp[i-1][i] = i
        
    for d in range(2, K+1):
        for i in range(K-d+1):
            j = i + d
            dp2[i][j] = 2e9
            for k in (dp[i][j-1], dp[i+1][j]):
                v = dp2[i][k] + dp2[k][j] + sums[j] - sums[i]
                if dp2[i][j] > v:
                    dp2[i][j] = v
                    dp[i][j] = k
    print(dp2[0][K])
    
    