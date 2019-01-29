import sys

def find(u, weight=0):
    if u == parent[u]:
        return (u, weight)
    
    parent[u], result = find(parent[u], weight + diff[u])
    return (parent[u], result)
        
def union(a, b, weight):
    ap, a_diff_from_root = find(a)
    bp, b_diff_from_root = find(b)
        
    if ap == bp:
        return
        
    if level[ap] > level[bp]:
        parent[bp] = ap
        
        diff[bp] += a_diff_from_root
        diff[bp] -= b_diff_from_root
        diff[bp] += weight
        
        level[ap] += level[bp]
        level[bp] = 1
    else:
        parent[ap] = bp
        
        diff[ap] -= a_diff_from_root
        diff[ap] += b_diff_from_root
        diff[ap] -= weight
        
        level[bp] += level[ap]
        level[ap] = 1

while True:
    N, M = map(int, sys.stdin.readline().split())
    
    if N == 0 and M == 0:
        break
    
    parent = [ i for i in range(N+1)]
    level = [ 1 for i in range(N+1)]
    diff = [ 0 for i in range(N+1)]
    
    for i in range(M):
        q = sys.stdin.readline().split()
        
        if len(q) >= 4:
            a, b, w = map(int, q[1:])
            union(a, b, w)
        else:
            a, b = map(int, q[1:])
            ap, a_weight = find(a)
            bp, b_weight = find(b)
            if ap == bp:
                print(b_weight-a_weight)
            else:
                print("UNKNOWN")