N, M = map(int, input().split())
querys = [int(x) for x in input().split()]
q = [ int(x) for x in range(1,N+1) ]
        
result = 0
for query in querys:
    N = len(q)
    
    while True:
        target = q.index(query)
        
        left_distance = target
        right_distance = N - target -1
        
        if left_distance == 0:
            q.pop(0)
            #del q[target]
            break
        
        if left_distance <= right_distance:
            q.append(q.pop(0))
            result += 1
        else:
            q.insert(0, q.pop())
            result += 1
    
print(result)
        
        
        
        

        
    