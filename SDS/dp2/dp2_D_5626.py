from sys import stdin

N = int(stdin.readline())

MOD = 1000000007
MAX_HEIGHT = 10000

altars = [ int(x) for x in stdin.readline().split()]
dp = [ [ 0 for _ in range(MAX_HEIGHT//2+2)] , [ 0 for _ in range(MAX_HEIGHT//2+2)] ]

cur_state = 0
before_state = 1

# 경우의 수가 0일것도 생각 하자
if altars[0] == 0 or altars[0] == -1:
    dp[before_state][1] = 1 
    
for i in range(N): # 모두 1씩 올려서 계산을 편하게
    if altars[i] != -1:
        altars[i] += 1
    
for i in range(1, N): # 어차피 양옆은 0 고정
    dp[cur_state] = [ 0 for _ in range(MAX_HEIGHT+1)]
    if altars[i] == -1:
        for j in range(1, MAX_HEIGHT//2+1): # 최대 높이는 MAX_HEIGHT / 2 만 되니까 (시간 감소)
            dp[cur_state][j] = (dp[before_state][j-1] + dp[before_state][j] + dp[before_state][j+1]) % MOD
    else:
        dp[cur_state][altars[i]] = (dp[before_state][altars[i]-1] + dp[before_state][altars[i]] + dp[before_state][altars[i]+1]) % MOD
    
    cur_state, before_state = before_state, cur_state

print(dp[before_state][1])