from sys import stdin

N, M = map(int, stdin.readline().split())

memorys = [ int(x) for x in stdin.readline().split()]
costs = [ int(x) for x in stdin.readline().split()]

# 띄엄 띄엄 있는 걸 고려하지 않았다
# dp[x][y]로 잡았을 때 x는 기기수 y는 cost의 메모리 최대
# dp[cost]로 잡아도 될까?
dp = [ 0 for _ in range(10001) ]

for i in range(N):
    for j in range(10000, -1, -1):
        if j-costs[i] >= 0:
            dp[j] = max(dp[j], dp[j-costs[i]] + memorys[i])
        
answer = 0
while answer <= 10001:
    if dp[answer] >= M:
        break
    answer += 1
    
print(answer)
        
        
