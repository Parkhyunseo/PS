for t in range(T):
    N = int(input())
    cards = map(int, input().split())
    
    get(0, N-1, 0)
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