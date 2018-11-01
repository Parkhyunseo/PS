text = list(raw_input())
alpha = [ -1 for _ in range(26) ]

for i in range(len(text)):
    if alpha[ord(text[i]) - ord('a')] == -1:
        alpha[ord(text[i]) - ord('a')] = i

print(' '.join( str(x) for x in alpha))
