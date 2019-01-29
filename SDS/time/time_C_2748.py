N = int(input())

t0 = 0
t1 = 1
for i in range(2, N+1):
    t0, t1 = t1, t0+t1
    
print(t1)
