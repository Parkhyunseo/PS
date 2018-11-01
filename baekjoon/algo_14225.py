N = int(input())
S = list(map(int, input().split()))
R = set()

for i in range(N):
    before = S[i]
    R.add(before)
    for j in range(i, N):
        before = before + S[j]
        R.add(before)
R = list(R)        
R.sort()

result = -1

for i in range(len(R)):
    if i != R[i]:
        result = i
        break
    
if result == -1:
    result = R[-1]+1
    
print(result)
    
        