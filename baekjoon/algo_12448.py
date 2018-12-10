T =int(input())

for _ in range(T):
    A = input()
    B = input()
    stack = []
    
    result = ""
    points = []
    point = 0
    
    while point < len(A) and point < len(B):
        if A[point] == B[point]:
            stack.append(A[point])
        else:
            result += A[point]
            if len(stack) > 0:
                pop = stack.pop()
                result += "*"
                
                while A[point] == pop and len(stack) > 0:
                    result += str(pop)
                    pop = stack.pop() 
                    
                    if A[point] != pop:
                        break
                
        point += 1
        
    if len(stack) > 0:
        result += "*"
                
    print(result)