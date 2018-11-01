N = input()
count = 0

for i in xrange(N):
    word = raw_input()
    alpha = [ False for _ in range(26) ]
    
    fail_flag = False
    
    pos = 0
    while pos < len(word):
        if alpha[ord(word[pos])-ord('a')] is False:
            alpha[ord(word[pos])-ord('a')] = True
            remember = word[pos]
            pos += 1
            while pos < len(word) and remember == word[pos]:
                pos += 1
        else:
            fail_flag = True
            break
    
    if fail_flag == False:
        count += 1
        
print count