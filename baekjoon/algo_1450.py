N, C = map(int, input().split())
items = [ int(x) for x in input().split()]

def dfs(here, c):
    result = 0
    if here < N-1:
        if c+items[here] <= C:
            result += dfs(here+1, c+items[here])
    
        result += dfs(here+1, c)
    
        return result
    else:
        if c+items[here] <=C:
            return 2
        else:
            return 1
    
print(dfs(0, 0))
        