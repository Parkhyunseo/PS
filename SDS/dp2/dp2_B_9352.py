A = '0'+input()
B = '0'+input()

dp = [ [ 0 for _ in range(len(B)) ] for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B)):
        if i == 0 and j ==0:
            dp[i][j] = 0
            continue
        
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])



stack = []
i, j = len(A)-1, len(B)-1

while True:
    if dp[i][j] == 0:
        break
    
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    elif dp[i][j] != dp[i-1][j-1]:
        stack.append(A[i])
        j -= 1
        i -= 1
        
print(dp[len(A)-1][len(B)-1])
print(''.join(reversed(stack)))

    