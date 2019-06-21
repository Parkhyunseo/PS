T = int(input())

dp = [ 0 for _ in range(100001)]
    
for i in range(2, 100001):
    if i % 2 == 0:
        dp[i] = dp[i//2] + 1
    else:
        dp[i] = dp[(i+1)//2] + 2

for t in range(T):
    n1, n2 = map(int ,input().split())
    
    result = 0
        
    for i in range(n1, n2+1):
        result += dp[i]
        
    print(result)
            