# readline은 마지막 개행 문자도 포함

A = '0'+input()
B = '0'+input()

dp = [ [ 0 for _ in range(len(B))] for _ in range(len(A))]

result = 0

for i in range(len(A)):
    for j in range(len(B)):
        if i == 0 or j ==0:
            dp[i][j] = 0
            continue
        
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            result = max(result, dp[i][j])

print(result)