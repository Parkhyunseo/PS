from sys import stdin

T = int(stdin.readline())

for t in range(T):
    N = int(stdin.readline())
    points = sorted([ int(x) for x in stdin.readline().split()])
    count = 0
    
    for i in range(N-2):
        k = i+2
        for j in range(i+1, N-1):
            diff = 2*points[j] - points[i]
            
            while k<N and points[k] < diff:
                k +=1
                
            if k == N:
                break 
            
            if diff == points[k]:
                count += 1

    print(count)