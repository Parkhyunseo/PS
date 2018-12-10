N, S = map(int, input().split())
A = [ int(x) for x in input().split()]
def dfs(here, cost):
    if here == N:
        if cost == S:
            return 1
        else:
            return 0
            
    return dfs(here+1, cost+A[here]) + dfs(here+1, cost)
result = dfs(0, 0)
print( result-1 if S is 0 else result )