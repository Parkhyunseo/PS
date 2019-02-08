from functools import lru_cache
T=int(input())

@lru_cache(maxsize=1000000)
def _pow(a, b):
    if b == 1:
        return a
        
    if b & 1 == 0:
        return _pow(a, b//2) * _pow(a, b//2)
    else:
        return _pow(a, b//2) * _pow(a, b//2) * a
        
for t in range(T):
    a, b = map(int, input().split())
    a = a % 10
    result = _pow(a, b) % 10
    if result == 0:
        print(10)
    else:
        print(result)