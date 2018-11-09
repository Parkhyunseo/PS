import sys

T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    recruits = []
    
    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
    
        recruits.append((a, b))
    
    recruits.sort(key=lambda x: (x[0], x[1]))
    
    max_b = 100001
    count = 0
    
    for i in range(N):
        a, b = recruits[i]
        if max_b > b:
            max_b = b
            count += 1
            
    print(count)