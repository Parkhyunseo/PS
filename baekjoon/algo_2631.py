import sys

N = int(sys.stdin.readline())
children = []
dp = [ 0 for _ in range(N)]
dp[0] = 1

for i in range(N):
    children.append(int(input()))

for i in range(1, N):
    dp[i] = 1
    for j in range(i):
        if children[j] < children[i] and dp[j] +1 > dp[i]:
            dp[i] = dp[j] + 1
            
#print(dp)
print(N-max(dp[1:]))

