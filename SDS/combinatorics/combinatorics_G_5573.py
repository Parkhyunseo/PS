H, W, N = map(int, input().split())

base = [ [ 0 for _ in range(W+2)] for _ in range(H+2)] 
dp = [ [ 0 for _ in range(W+2)] for _ in range(H+2)]

for h in range(1, H+1):
    line = [int(x) for x in input().split()]
    for w in range(1, W+1):
        base[h][w] = line[w-1]

dp[1][1] = N-1

for h in range(1, H+1):
    for w in range(1, W+1):
        if dp[h][w] == 0:
            continue
        
        dp[h+1][w] += dp[h][w] // 2
        dp[h][w+1] += dp[h][w] // 2
        
        if dp[h][w] % 2 != 0:
            if base[h][w] == 1:
                dp[h][w+1] += 1
            else:
                dp[h+1][w] += 1
                
        base[h][w] = (base[h][w] + dp[h][w]) % 2
        
        
x, y = 1, 1

while x <= W and y <= H:
    if base[y][x] == 1:
        x += 1
    else:
        y += 1
        
print(y, x)
    
            
            
        