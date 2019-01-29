import bisect

N = int(input())
a, b, c, d = [], [], [], []
for i in range(N):
    q,w,e,r = map(int, input().split())
    a.append(q)
    b.append(w)
    c.append(e)
    d.append(r)
    
a_plus_b = []

for i in range(N):
    for j in range(N):
        a_plus_b.append(a[i] + b[j])

a_plus_b.sort()
count = 0

for i in range(N):
    for j in range(N):
        lo = bisect.bisect_left(a_plus_b, -c[i]-d[j])
        hi = bisect.bisect_left(a_plus_b, -c[i]-d[j])
        
        if lo < len(a_plus_b):
            if a_plus_b[lo] -c[i]-d[j] == 0:
                count += hi-lo
        
print(count)