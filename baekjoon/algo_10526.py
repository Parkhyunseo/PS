N = int(input())
MAX = 987654321
#visited = [ False for _ in range(N)]
W = []
DP = [ [ 0 for _ in range(2**N)] for _ in range(N)]

def tsp(current, visited):
    if visited == (( 1 << N) -1):
        if W[current][visited] + 
        if W[current][0] == 0:
            return MAX
        else:
            return W[current][0];
        
    if DP[current][visited] != 0:
        return DP[current][visited]
        
    result = MAX
    
    for i in range(1, N):
        if visited & (1 << i):
            continue
        
        if W[current][i] == 0:
            continue
        
        result = min(result, tsp(i, visited | (1 << i)) + W[current][i])
        
    DP[current][visited] = result    
    return DP[current][visited]

for i in range(N):
    line = [ int(x) for x in input().split()]
    W.append(line)
    
print(tsp(0, 1))
    
    