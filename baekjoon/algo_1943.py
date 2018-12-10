for t in range(3):
    N = int(input())
    
    coins = []
    total = 0
    # N개 코인을 이용했을 때 내가 가지고 있는 돈
    for i in range(N):
        val, count = map(int, input().split())
        coins.append((val, count))
        total += val*count
        
    dp = [ 0 for _ in range(100001)]
    
    val, count = coins[0]
    for c in range(1,count+1):
        dp[val*c] = 1
    
    for i in range(1, len(coins)):
        val, count = coins[i]
        for j in range(total//2+1, 0, -1):
            for c in range(1, count+1):
                if j-val*count > 0 and dp[j-val*count] == 1:
                    dp[j] = 1
            
    print(dp[total//2])