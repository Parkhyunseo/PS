alpha = map(int, raw_input().split())
text = list(raw_input())

alpha.sort()

result = []

for i in range(3):
    result.append(alpha[ord(text[i])-ord('A')])
    
print(' '.join([ str(x) for x in result]))

