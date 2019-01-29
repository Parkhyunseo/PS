from sys import stdin
N=map(int, stdin.readlines())
for n in N:
    C = 1
    K = 0
    while True:
        K = 10*K+1
        if K % n == 0:
            break
        C += 1
    print(C)
        

        
