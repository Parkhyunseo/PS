N = int(input())
wines = []
dp = [ 0 for _ in range(N)]

for n in range(N):
    wines.append(int(input()))

dp[0] = wines[0]
if N >= 2:
    dp[1] = wines[0] + wines[1]
    if N >= 3:
        dp[2] = max(dp[1], wines[1] + wines[2], wines[0]+wines[2])

for i in range(3, N):
    dp[i] = max(dp[i-2] + wines[i],\
    dp[i-3] + wines[i] + wines[i-1], \
    dp[i-1])
print(dp[N-1])