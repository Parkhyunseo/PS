N = int(input())
P = [ int(x) for x in input().split()]
dp =  [ 1 for _ in range(N)]
m = 0

for i in range(N):
    for j in range(i):
        if P[j] < P[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
        
        if m < dp[i]:
            m = dp[i]

print(m)