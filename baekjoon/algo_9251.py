TEXT1 = '0'+input()
TEXT2 = '0'+input()
DP = [ [ 0 for _ in range(len(TEXT2))] for _ in range(len(TEXT1))]
for i in range(len(TEXT1)):
    for j in range(len(TEXT2)):
        if i==0 and j==0:
            continue
        
        if TEXT1[i] == TEXT2[j]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
            -
print(DP[len(TEXT1)-1][len(TEXT2)-1])