N, M = map(int, raw_input().split())
dna = []
result = []
result_count = 0

for n in range(N):
    dna.append(list(raw_input()))
    
for m in range(M):
    arr = [ 0 for _ in range(26)]
    for n in range(N):
        arr[ord(dna[n][m]) - ord('A')] += 1
        
    max_index = -1
    max_value = max(arr)
    for i in range(26):
        if arr[i] == max_value:
            max_index = i
            break
        
    for n in range(N):
        if ord(dna[n][m]) - ord('A') != max_index:
            result_count += 1
        
    result.append(chr(ord('A') + max_index))
    
print(''.join(result))
print(result_count)