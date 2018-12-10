from sys import stdin

while True:
    read = ''
    x = ''
    flag = False
    while "#" not in x:
        x = stdin.readline()
        if x == '':
            flag = True
            break
        
        if x is not "#":
            read += x
    if flag:
        exit()
    x = ''
    
    while "#" not in x:
        x = stdin.readline()
        if x is not "#":
            read += x
            
    split = read.split("#")
    
    A = split[0].split()
    A.insert(0,'0')
    B = split[1].split()
    B.insert(0,'1')
    
    result = [ [ 0 for _ in range(len(B))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B)):
            if i == 0 and j ==0:
                continue
            
            if A[i] == B[j]:
                result[i][j] = result[i-1][j-1]+1
            else:
                result[i][j] = max(result[i-1][j], result[i][j-1])
                
    i = len(A)-1
    j = len(B)-1
    
    ans = []
    
    while result[i][j] != 0:
        if result[i][j]  == result[i][j-1]:
            j -= 1
        elif result[i][j] == result[i-1][j]:
            i -= 1
        elif result[i][j] -1 == result[i-1][j-1]:
            ans.append(A[i])
            i -= 1
            j -= 1
            
        if i < 0 or j < 0:
            break
            
    print(' '.join(reversed(ans)))
        
    