A='0' + input()
B='0' + input()
AL = len(A)
BL = len(B)
LCS = [ [ 0 for _ in range(BL)] for _ in range(AL)]

for i in range(AL):
    for j in range(BL):
        if i == 0 and j ==0:
            continue
        
        if A[i] == B[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])

print(LCS[AL-1][BL-1])
