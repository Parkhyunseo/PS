from sys import stdin
count = [ 0 for _ in range(10001)]
N = int(stdin.readline())
for _ in range(N):
    n = int(stdin.readline())
    count[n] += 1
    
for i in range(10001):
    while count[i] > 0:
        print(i)
        count[i] -= 1
        