N = input()
line = map(int, raw_input().split())
result = []

for i in reversed(range(N)):
    if len(result) == 0:
        result.append(i+1)
    else:
        result = result[:line[i]] + [i+1] + result[line[i]:]
    
print(" ".join( str(x) for x in result))
