# 어차피 Cycle이라서 모든 곳에서 출발 할 필요가 없다.
N = int(input())
MAX = 99999999
dp = [ [ 0 for _ in range(2**N)] for _ in range(N)]
table = [ [] for _ in range(N)]

for i in range(N):
    table[i] = [ int(x) for x in input().split() ]
    
done = list(input())
P = int(input())

state = 0

for i in range(len(done)):
    if done[i] == 'Y':
        state += i << N-i
    else:
        state += 0 << N-i
    
def solve(state, depth):
    if depth == P:
        return 0
    
    if dp[state] != 0:
        return dp[state]
    
    result = MAX
    
    for here in range(N):
        if done & ( 0 << there): # 안 켜져 있으면 continue
            continue
        
        for there in range(N):
            if done & ( 1 << there): # 켜져 있으면 continue
                continue
            
            if table[here][there] == 0: # 
                continue
            
            result = min(result, solve(state | ( 1 << there), depth+1) + table[here][there])

    dp[state] = result
    return result
    
answer = solve(0, 1, 0)

print(answer)