N = int(input())
lines = [ int(x) for x in input().split()]
result = [lines[0]]

def low_bound(start, end, find):
    while start < end:
        mid = (start + end) >> 1
        
        if find > result[mid]:
            start = mid + 1
        else:
            end = mid
  
    return end + 1

# 길이
D = [ 1 for _ in range(N) ]

for i in range(N):
    if result[-1] < lines[i]:
        result.append(lines[i])
        D[i] = len(result)-1
    else:
        ans = low_bound(0, len(result)-1, lines[i])
        result[ans-1] = lines[i]
        D[i] = ans-1
        
print(len(result))

find = len(result)-1
ans = []
for i in range(N-1, -1, -1):
    if D[i] == find:
        ans.insert(0, lines[i])
        find -= 1
   
print(' '.join([ str(x) for x in ans]))