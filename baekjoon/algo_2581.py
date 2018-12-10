M=int(input())
N=int(input())
table = [ True for _ in range(10001)]
table[1] = False

def eratos():
    for i in range(2, 101):
        if table[i]:
            for j in range(i*2, 10001, i):
                table[j] = False

m = 10001
accum = 0

eratos()

for i in range(M, N+1):
    if table[i]:
        accum += i
        m = min(m, i)
     
if accum != 0:
    print(accum)
    print(m)
else:
    print(-1)
    