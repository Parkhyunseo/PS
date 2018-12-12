N = int(input())
a, b, c = 1, 1, 1
for i in range(2, N+1):
    d, e, f = b+c, a+c, a+b+c
    a, b, c = d, e, f

print((a+b+c)%9901)