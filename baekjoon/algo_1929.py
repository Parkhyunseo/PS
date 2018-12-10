M, N = map(int, input().split())

table = [ True for _ in range(N+1)]
table[1] = False
def eratos():
    for i in range(2, int(N**0.5)+1):
        if table[i]:
            for j in range(i+i, N+1, i):
                table[j] = False
                
eratos()
for i in range(M, N+1):
    if table[i]:
        print(i)