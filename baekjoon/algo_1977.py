M = int(input())
N = int(input())

result = 10001
sums = 0
i=0

while i*i <= N:
    if i*i >= M and i*i <= N:
        result = min(result, i*i)
        sums += i*i
    i+=1
        
if sums == 0:
    print(-1)
else:
    print(sums)
    print(result)