W, H = map(int, input().split())

MOD = 100000

"""
# x, y = 0 안갔다. 1, 한번 갔다. 2, 2번이상 움직였다.
# (0, 1) (0, 2), (1, 0), (2, 0)
def solve(w, h, x, y):
    if w-x < 1 and x == 2:
        return 0
        
    if h-y < 1 and y == 2:
        return 0
    
    
    print(w, h, x, y)
    
    if w == 1 or h == 1:
        print(w, h, x, y, 'count')
        return 1
    
    if x == 2:
        return  (solve(w-1, h, 1, 0) +  solve(w-1, h, 2, 0)) % MOD
    elif x == 1:
        return solve(w-1, h, 0, 2) % MOD
        
    if y == 2:
        return (solve(w, h-1, 0, 1) + solve(w, h-1, 0, 2)) % MOD
    elif y == 1:
        return solve(w, h-1, 2, 0) % MOD

        
result = 0

if W >= 3:
    result += solve(W,H,2,0)
print('')

result += solve(W,H,1,0)
print('')
if H >= 3:
    result += solve(W,H,0,2)
print('')    
result += solve(W,H,0,1)
print(result)
"""


# 0 - x 1번
# 1 - x 2번
# 2 - y 1번
# 3 - y 2번
dp = [ [ [0, 0, 0, 0]  for _ in range(W+1)] for _ in range(H+1)]

for h in range(2, H+1):
    dp[h][1][3] = 1
    dp[h][1][2] = 1
    #dp[h][1][3] = 1

for w in range(2, W+1):
    dp[1][w][1] = 1
    dp[1][w][0] = 1
    #dp[1][w][1] = 1

for h in range(2, H+1):
    for w in range(2, W+1):
        dp[h][w][0] = dp[h][w-1][3] % MOD
        dp[h][w][1] = (dp[h][w-1][0] + dp[h][w-1][1]) % MOD
        dp[h][w][2] = dp[h-1][w][1] % MOD
        dp[h][w][3] = (dp[h-1][w][2] + dp[h-1][w][3]) % MOD
    #print(dp[h])
print(sum(dp[H][W])% MOD)