N, M, K = map(int, input().split())
arr = []
seg = [ 0 for _ in range(4*N)]

def init(a, seg, node, start, end):
    if start == end:
        seg[node] = a[start]    
        return seg[node] 
    else:
        mid = (start + end) >> 1
        seg[node] = init(a, seg, node*2, start, mid) + init(a, seg, node*2+1, mid+1, end)
        return seg[node]

def update(pos, node, x, y):
    if y < pos or pos < x:
        return 0
    
    if x==y:
        return seg[node]
    
    mid = (x+y) >> 1
    seg[node] = update(pos, node*2, x, mid) + update(pos, node*2+1, mid+1, y)
    return seg[node]
    
def query(lo, hi, node, x, y):
    if y < lo or x > hi:
        return 0
        
    if lo <= x and y <= hi:
        return seg[node]
    
    mid = (x+y) >> 1    
    return query(lo, hi, node*2, x, mid) + query(lo, hi, node*2 + 1, mid+1 , y)

for i in range(N):
    arr.append(int(input()))
    
init(arr, seg, 1, 0, N-1)
    
for j in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b-1, c, 0, N-1)
    else:
        result = query(b-1, c-1, 0, 0, N-1)
        print(result)
        
    
        