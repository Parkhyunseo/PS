from sys import stdin

N = int(stdin.readline())
result = [ 0 for i in range(2000001)]
for n in range(N):
    num = int(stdin.readline())
    if num >= 0:
        result[num] = 1 
    else:
        num *= -1
        num += 1000000
        result[num] = 1 

for n in range(2000000, 1000000, -1):
    if result[n] == 1:
        n -= 1000000
        n *= -1
        print(n)
        
for n in range(1000001):
    if result[n] == 1:
        print(n)
    
    