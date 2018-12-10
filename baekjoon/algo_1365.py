from bisect import bisect_left

N = int(input())
lines = [ int(x) for x in input().split()]
result = [lines[0]]

for i in range(N):
    if result[-1] < lines[i]:
        result.append(lines[i])
    else:
        ans = bisect_left(result, lines[i], 0, len(result))
        result[ans] = lines[i]
    #print(result)
print(N-len(result))