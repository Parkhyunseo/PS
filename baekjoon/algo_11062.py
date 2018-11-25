from sys import stdin

def solve(turn: bool, x:int, y:int) -> int:
    if x == y:
        if turn == 0:
            return cards[x] 
        else:
            return 0 
    
    if dp[x][y][turn] is not -1:
        return dp[x][y][turn]
    
    if turn == 0:
        dp[x][y][turn] = max(solve(not turn, x+1, y) + cards[x], solve(not turn, x, y-1) + cards[y])
    else:
        dp[x][y][turn] = min(solve(not turn, x+1, y), solve(not turn, x, y-1))
    
    return dp[x][y][turn]

T = int(stdin.readline())
for t in range(T):
    N = int(stdin.readline())
    cards =list(map(int, stdin.readline().split()))
    dp = [ [ [-1, -1] for _ in range(N)] for _ in range(N)]
    result = solve(0, 0, N-1)
    print(result)