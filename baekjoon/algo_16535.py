N = int(input())
A = list(map(int, input().split()))
dp = [ [-1 for _ in range(N)] for _ in range(N)]

i = 0
count = 0

def solve(l:int, r:int) -> int:
    if N <= l or N <= r:
        return 0
        
    if dp[l][r] != -1:
        return dp[l][r]
        
    score = 0
    
    if r <= l:
        return score
        
    num = A[l]
    for i in range(l+1, r+1):
        if A[i] == num:
            score = max(score, 2+solve(l+1, i-1)+solve(i+1, r))
            
    score = max(score, solve(l+1, r))
    dp[l][r] = score
    return score
    
print(solve(0, N-1))