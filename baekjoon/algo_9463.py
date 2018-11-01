T = int(input())

def update(pos, node, x, y):
    if y < pos or pos < x:
        return seg[node]
        
    if x == y:
        seg[node] = 1
        return seg[node]
    
    mid = (x + y) >> 1
    seg[node] = update(pos, node*2, x, mid) + update(pos, node*2+1, mid+1, y)
    return seg[node]        

def query(lo, hi, node, x, y):
    if y < lo or hi < x:
        return 0
    
    if lo <= x and y <= hi:
        return seg[node]
        
    mid = (x+y) >> 1
    return query(lo, hi, node*2, x, mid) + query(lo, hi, node*2 + 1, mid + 1, y)
    

for t in range(T):
    N = int(input())
    temp= list(map(int, input().split()))
    temp.insert(0, 0)

    A = [ 0 for _ in range(N+1)]
    for n in range(1, N+1):
        A[temp[n]] = n
    
    temp = list(map(int, input().split()))
    temp.insert(0, 0)
    
    B = [ 0 for _ in range(N+1)]
    for n in range(1, N+1):
        B[n] = A[temp[n]]
    
    seg = [ 0 for _ in range(4*N+1)]
    
    result = 0
    
    r = 0
    for i in range(1, N+1):
        r += B[i] - 1 - query(1, B[i], 1, 1, N)
        update(B[i], 1, 1, N)
    
    print(r)
