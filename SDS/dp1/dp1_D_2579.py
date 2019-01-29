from sys import stdin

N = int(stdin.readline())
A = [int(x) for x in stdin.readlines()]
#  이 계단까지 오는데 최댓값
# 안밟았다, 처음 밟는다. 두번째로 밟았다.
#dp = [ [0, 0, 0] for _ in range(N+1)]
dp = [ 0 for _ in range(N)]
# 연속으로?
# 그냥?



"""
for i in range(1, N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + A[i]
    dp[i][2] = dp[i-1][1] + A[i]
""" 
dp[0] = A[0]
dp[1] = A[0]+A[1]
dp[2] = max(A[1]+A[2], A[0]+A[2])
for i in range(3, N):
    dp[i] = max(A[i] + A[i-1] + dp[i-3], A[i]+dp[i-2])
    
print(dp[N-1])

"""
N = input()
arr = []
mem = [ 0 for _ in xrange(N)]

for n in xrange(N):
    arr.append(input())

def descend(i):
    if mem[i] != 0:
        return mem[i]
        
    if i == 0:
        return arr[i]
    elif i < 0:
        return 0
    
    mem[i] = max(arr[i] + arr[i-1] + descend(i-3), arr[i] + descend(i-2))
    
    return mem[i]

print(descend(N-1))
"""