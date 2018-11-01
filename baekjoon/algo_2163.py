N, M =map(int, input().split())

dp = [ [ -1 for _ in range(N) ] for _ in range(M)]

def divide(n, m):
    if dp[n][m] != -1:
        return dp[n][m]
    
    if n == 0 and m == 0:
        return 0
    
    nx = n // 2
    ny = n // 2
    mx = m // 2
    my = m // 2
    
    if n % 2 != 0:
        ny = n - nx
    
    if m % 2 != 0:
        my = m - mx
    
    if n == 0:
        dp[n][m] = divide(nx, 0) + divide(ny, 0) + 1
    elif m == 0:
        dp[n][m] = divide(0, mx) + divide(0, my) + 1
    else:
        dp[n][m] = divide(nx, mx) + divide(ny, mx) + divide(nx, my) + divide(ny, my) + 1
        
    return dp[n][m]
    
print(divide(N-1, M-1))