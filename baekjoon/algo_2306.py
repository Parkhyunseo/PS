dna = input()
N = len(dna)

dp = [ [ -1 for _ in range(N)] for _ in range(N)]

def solve(s, e):
    if dp[s][e] != -1:
        return dp[s][e]
        
    dp[s][e] = 0
        
    if (dna[s] == 'a' and dna[e] == 't') or (dna[s] == 'g' and dna[e] == 'c'):
        dp[s][e] = solve(s+1, e-1) + 2
    
    for i in range(s, e):
        dp[s][e] = max(dp[s][e], solve(s, i) + solve(i+1, e))
        
    return dp[s][e]

print(solve(0, N-1))