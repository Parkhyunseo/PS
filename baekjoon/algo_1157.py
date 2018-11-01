text = list(raw_input())
alpha = [ 0 for _ in range(26) ]
max_value = 0

for i in range(len(text)):
    if ord(text[i]) >= ord('a'):
        alpha[ord(text[i]) - ord('a')] += 1
        max_value = max(max_value, alpha[ord(text[i]) - ord('a')])
    else:
        alpha[ord(text[i]) - ord('A')] += 1
        max_value = max(max_value, alpha[ord(text[i]) - ord('A')])
        
flag = False
result = ''

for i in range(26):
    if max_value == alpha[i]:
        if flag:
            result = '?'
        else:
            result = chr(ord('A') + i)
            flag = True
    
print result