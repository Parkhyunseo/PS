from bisect import bisect_left

N = int(input())
lines = [ int(x) for x in input().split()]
result = [lines[0]]

# 길이
D = [ 1 for _ in range(N) ]

for i in range(N):
    if result[-1] < lines[i]:
        result.append(lines[i])
        D[i] = len(result)-1
    else:
        ans = bisect_left(result, lines[i])
        result[ans] = lines[i]
        D[i] = ans
        
print(len(result))

find = len(result)-1
ans = []
for i in range(N-1, -1, -1):
    if D[i] == find:
        ans.insert(0, lines[i])
        find -= 1
   
print(' '.join([ str(x) for x in ans]))