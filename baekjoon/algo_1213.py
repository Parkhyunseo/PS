name=raw_input()

alpha = [ 0 for _ in range(26)]

for i in xrange(len(name)):
    alpha[ord(name[i]) - ord('A')] += 1
    
result = list(name)
if len(name) & 1 == 1:
    odd_num = -1
    for i in xrange(len(alpha)):
        if alpha[i] & 1 == 1:
            if odd_num == -1:
                odd_num = i
            else:
                print "I'm Sorry Hansoo"
                break 
    
    if odd_num != -1:
        pos = 0
        for i in xrange(len(alpha)):
            if alpha[i] & 1 == 0:
                while alpha[i] == 0 and pos < len(name):
                    result[pos] = chr(i + ord('A'))
                    result[len(name)-pos-1] = chr(i + ord('A'))
                    pos += 1
                    alpha[i] -= 2
                    
        while alpha[odd_num] != 1 and pos < len(name):
            result[pos] = chr(i + ord('A'))
            result[len(name)-pos-1] = chr(i + ord('A'))
            pos += 1
            alpha[odd_num] -= 2
            
        result[pos] = alpha[odd_num]
            
else:
    pos = 0
    for i in xrange(len(alpha)):
        if alpha[i] & 1 == 1:
            print "I'm Sorry Hansoo"
            break
        else:
            while alpha[i] != 0 and pos < len(name):
                result[pos] = chr(i + ord('A'))
                result[len(name)-pos-1] = chr(i + ord('A'))
                pos += 1
                alpha[i] -= 2
                
print(''.join(result))