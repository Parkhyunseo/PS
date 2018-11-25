from sys import stdin
N, M, K = map(int, stdin.readline().split())
arr = []
seg = [ 0 for _ in range(4*N)]

def init(a, seg, node, start, end):
    if start == end:
        seg[node] = a[start]    
        return seg[node] 
        
    mid = (start + end) >> 1
    seg[node] = init(a, seg, node*2, start, mid) + init(a, seg, node*2+1, mid+1, end)
    return seg[node]

def update(node, s, e, index, diff):
    global seg
    
    if not ( s <= index and index <= e):
        return

    seg[node] += diff
    
    if s != e:
        mid = (s+e) >> 1
        update(node*2, s, mid, index, diff)
        update(node*2+1, mid+1, e, index, diff)
    
def query(s, e, node, lo, hi):
    global seg
    
    if lo > e or s > hi:
        return 0
        
    if lo <= s and e <= hi:
        return seg[node]
    
    mid = (s+e) >> 1    
    return query(s, mid, node*2, lo, hi) + query(mid+1, e, node*2+1, lo, hi)

for i in range(N):
    arr.append(int(input()))
    
init(arr, seg, 1, 0, N-1)

for j in range(M+K):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        diff = c - arr[b-1]
        arr[b-1] = c
        update(1, 0, N- 1, b-1, diff)
        #print(seg)
    else:
        result = query(0, N-1, 1, b-1, c-1)
        print(result)
        
    
        