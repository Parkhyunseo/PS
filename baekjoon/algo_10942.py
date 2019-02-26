from sys import stdin

N = int(stdin.readline())
nums = [ 0 ] + [ int(x) for x in stdin.readline().split() ]
dp = [ [ -1 for _ in range(N+1) ] for _ in range(N+1) ]

M = int(stdin.readline())

def isPalindrome(s, e):
    if dp[s][e] != -1:
        return dp[s][e]
    
    if s == e:
        dp[s][e] = 1
    else:
        if nums[s] == nums[e]:
            if s + 1 == e:
                dp[s][e] = 1
            else:
                dp[s][e] = isPalindrome(s+1, e-1)
        else:
            dp[s][e] = 0
    
    return dp[s][e]

for m in range(M):
    print(isPalindrome(*map(int, stdin.readline().split())))
    
