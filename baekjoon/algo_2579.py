N = input()
arr = []
mem = [ 0 for _ in xrange(N)]

for n in xrange(N):
    arr.append(input())

def descend(i):
    if mem[i] != 0:
        return mem[i]
        
    if i == 0:
        return arr[i]
    elif i < 0:
        return 0
    
    mem[i] = max(arr[i] + arr[i-1] + descend(i-3), arr[i] + descend(i-2))
    
    return mem[i]

print(descend(N-1))
