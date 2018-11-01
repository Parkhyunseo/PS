N = int(input())
dp = [ [-1, -1] for _ in range(N)]

def topdown(i, num):
    if dp[i][num] != -1:
        return dp[i][num]
    
    if i == 0:
        if num == 1:
            return 1
        else:
            return 0
            
    if num == 0:
        dp[i][num] = topdown(i-1, 1) + topdown(i-1, 0)
    else:
        dp[i][num] =  topdown(i-1, 0)
    return dp[i][num]
    
print(topdown(N-1, 0) + topdown(N-1, 1))