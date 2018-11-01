#for i in range(10):
import copy

N = int(input())
vec = []

def happy(n):
    
    if n == 1:
        print("HAPPY")
        return
    
    for v in vec:
        if n == v:
            print("UNHAPPY")
            return
    
    vec.append(n)
    
    cop = copy.deepcopy(n)
    result = 0
    
    while cop:
        result += (cop%10) * (cop%10)
        cop //= 10
    
    happy(result)
    
happy(N)