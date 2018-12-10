N = int(input())
lines = []

for i in range(N):
    a, b = map(int, input().split())
    lines.append((a, b))
    
lines.sort(key=lambda x:x[0])

dp = [ 1 for _ in range(N)]
m = 0

for i in range(N):
    for j in range(i):
        if lines[j][1] < lines[i][1] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
    
    if m < dp[i]:
        m = dp[i]
        
print(N-m)