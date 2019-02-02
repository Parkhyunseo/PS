# Python 할 때 항상 재귀 깊이 생각
from sys import stdin, setrecursionlimit
setrecursionlimit(1000000000)

pos = [ int(x) for x in stdin.readline().split()]
if len(pos) >= 1:
    pos = pos[:-1]
dp = [ [ [ -1 for _ in range(len(pos)+1)] for _ in range(5)] for _ in range(5)]
# dp[x][y][k] 지금 k번쨰에 발이 (x, y)에 위치할 최소 값

def solve(left, right, count):
    if count >= len(pos):
        return 0

    temp = 400001
        
    if dp[left][right][count] != -1:
        return dp[left][right][count]
    
    # 안 해도 되나
    #if left == 0 and right == 0:
    #    dp[left][right][count] = solve(pos[count], right, count+1) +2
    #    return dp[left][right][count]
    
    # 두 발 중 밟아야할 곳에 이미 발이 위치해 있다면
    if left == pos[count] or right == pos[count]:
        dp[left][right][count] = solve(left, right, count+1) + 1
        return dp[left][right][count]
    
    # 왼발 중앙
    if left == 0:
        temp =  min(temp, solve(pos[count], right, count+1) + 2)
    elif (left == 1 and pos[count] == 3) or \
        (left == 2 and pos[count] == 4) or \
        (left == 3 and pos[count] == 1) or\
        (left == 4 and pos[count] == 2):
        temp =  min(temp, solve(pos[count], right, count+1) + 4)
    else:
        temp = min(temp, solve(pos[count], right, count+1) + 3)
        
    # 오른발 중앙
    if right == 0:
        temp = min(temp, solve(left, pos[count], count+1) + 2)
    elif (right == 1 and pos[count] == 3) or \
        (right == 2 and pos[count] == 4) or \
        (right == 3 and pos[count] == 1) or\
        (right == 4 and pos[count] == 2):
        temp = min(temp, solve(left, pos[count], count+1) + 4)
    else:
        temp = min(temp, solve(left, pos[count], count+1) + 3)
        
    
    dp[left][right][count] = temp
    return temp


print(solve(0, 0, 0))