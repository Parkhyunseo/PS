# Python 할 때 항상 재귀 깊이 생각
from sys import stdin, setrecursionlimit
setrecursionlimit(1000000000)

N = int(stdin.readline())
W = int(stdin.readline())
pos = [(-1, -1)]

for i in range(W):
    y, x = map(int, stdin.readline().split())
    pos.append((y, x))
    
dp = [ [ -1 for _ in range(W+1)] for _ in range(W+1)]
who = [ [ -1 for _ in range(W+1)] for _ in range(W+1)]

def get_manhatten_distance(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

def get_minimum_distance(first, second, count):
    if count >= len(pos):
        return 0

    if dp[first][second] != -1:
        return dp[first][second]
    
    f, s = 0, 0
    
    if first == 0:
        f = get_minimum_distance(count, second, count+1) + get_manhatten_distance((1, 1), pos[count])
    else:
        f = get_minimum_distance(count, second, count+1) + get_manhatten_distance(pos[first], pos[count])
        
    if second == 0:
        s = get_minimum_distance(first, count, count+1) + get_manhatten_distance((N, N), pos[count])
    else:
        s = get_minimum_distance(first, count, count+1) + get_manhatten_distance(pos[second], pos[count])
    
    if f < s:
        who[first][second] = 1
    else:
        who[first][second] = 2
        
    dp[first][second] = min(f, s)
    
    return dp[first][second]
    
print(get_minimum_distance(0, 0, 1))

f, s, c = 0, 0, 1
while True:
    if c > W:
        break
    
    print(who[f][s])

    if f == 0:
        first = dp[c][s] + get_manhatten_distance(pos[c], (1, 1))
    else:
        first = dp[c][s] + get_manhatten_distance(pos[c], pos[f])
        
    if s ==0:
        second = dp[f][c] +  get_manhatten_distance(pos[c], (N,N))
    else:
        second = dp[f][c] +  get_manhatten_distance(pos[c], pos[s])
    
    if first < second:
        f = c 
    else:
        s = c
        
    c += 1
