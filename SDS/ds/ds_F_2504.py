import sys

text = list(input())
stack = []

small = 0
big = 0

temp = 1
total = 0

for i in range(len(text)):
    if text[i] == '(':
        stack.append('(')
        small += 1
        temp *= 2
        if i < len(text) - 1:
            if text[i+1] == ')':
                total += temp
                
    elif text[i] == '[':
        stack.append('[')
        big += 1
        temp *= 3
        
        if i < len(text) - 1:
            if text[i+1] == ']':
                total += temp
            
    elif text[i] == ')':
        if len(stack) <= 0:
            print(0)
            sys.exit()
            
        top = stack.pop()
        
        if top != '(':
            print(0)
            sys.exit()
        
        small -= 1
        temp //= 2
    else:
        if len(stack) <= 0:
            print(0)
            sys.exit()
            
        top = stack.pop()
        
        if top != '[':
            print(0)
            sys.exit()

        big -= 1
        temp //= 3 

if len(stack) > 0 or small !=0  or big !=0:
    print(0)
else:
    print(total)
        
        
    
    