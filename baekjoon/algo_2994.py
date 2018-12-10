T, N = map(int, input())
breaks = [ int(x) for x in input().split() ]
dp = [ [ 0 for _ in range(N) ]] for _ in range(T)]

for t in range(T):
    for n in range(N):
        if dp[t][n]
        dp[t][n] = 