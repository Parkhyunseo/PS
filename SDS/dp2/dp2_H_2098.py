# 어차피 Cycle이라서 모든 곳에서 출발 할 필요가 없다.

N = int(input())
MAX = 99999999
dp = [ [ 0 for _ in range(2**N)] for _ in range(N)]
table = [ [] for _ in range(N)]

for i in range(N):
    table[i] = [ int(x) for x in input().split() ]
    
def solve(here, visited, start):
    if visited == 2**N-1:
        if table[here][0] == 0:
            return MAX
        else:
            return table[here][0]
    
    if dp[here][visited] != 0:
        return dp[here][visited]
    
    result = MAX
    
    for there in range(N):
        if visited & ( 1 << there) :
            continue
        
        if table[here][there] == 0:
            continue
        
        result = min(result, solve(there, visited | ( 1 << there), start) + table[here][there])

    dp[here][visited] = result
    return result
    
answer = solve(0, 1, 0)

print(answer)