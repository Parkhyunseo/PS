from sys import stdin, exit

# root는 1개
# inedge 는 1개
# edge = node_count -= 1
case = 1
while True:
    while True:
        flag = False
        line = [int(x) for x in stdin.readline().split()]
         
        for i in range(0, len(line), 2):
            inedge = [ 0 for _ in range(10001)]
            outedge = [ 0 for _ in range(10001)]
            exist = [ 0 for _ in range(10001)]
            
            check = True
            root = -1
            edge = 0
            node_count = 0
            MAX_VALUE = 0
            MIN_VALUE = 100000000
    
            if line[i] == -1:
                exit()
                
            if line[i] == 0:
                flag = True
                break
            
            inedge[line[i+1]] += 1
            outedge[line[i]] += 1
            
            exist[line[i]] += 1
            exist[line[i+1]] += 1
            
            MAX_VALUE = max(MAX_VALUE, line[i], line[i+1])
            MIN_VALUE = min(MIN_VALUE, line[i], line[i+1])
            edge += 1
        
        if flag:
            break
    
    # 1번
    for i in range(MIN_VALUE, MAX_VALUE+1):
        if inedge[i] == 0 and outedge[i] > 0:
            if root != -1:
                check = False
                break
            root = i
    # 2번
    for i in range(MIN_VALUE, MAX_VALUE+1):
        if inedge[i] > 1:
            check = False

    # 3 번
    for i in range(MIN_VALUE, MAX_VALUE+1):
        if exist[i] != 0:
            node_count += 1

    if node_count-1 != edge:
        check = False
        
    if check :
        print("Case {0} is a tree.".format(case))
    else:
        print("Case {0} is not a tree.".format(case))
    
    case += 1
    