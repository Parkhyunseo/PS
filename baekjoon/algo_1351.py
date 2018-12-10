N, P, Q = map(int, input().split())
d = dict()
def f(x):
    if x in d:
        return d[x]
        
    if x == 0:
        return 1
        
    d[x] = f(x//P) + f(x//Q)
    return d[x]
    
print(f(N))