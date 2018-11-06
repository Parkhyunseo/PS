"""w, n = map(int, input().split())
A = list(map(int, input().split()))
mark = [ False for i in range(800000)]
find =False

for j in range(1, n-2):
    for k in range(j+1, n-1):
        for l in range(k+1, n):
            if w-A[j]-A[k]-A[l] > 0:
                mark[w-A[j]-A[k]-A[l]] = True
    for i in range(j):
        if mark[A[i]]:
            find = True
        #i += 1
    
if find:
    print("YES")
else:
    print("NO")
"""
w, n = map(int, input().split())
A = list(map(int, input().split()))
mark = [ False for i in range(800000)]
find = False

ij = []
for k in range(2, n-1):
    for l in range(k+1, n):
        if w-A[k]-A[l] > 0:
            mark[w-A[k]-A[l]] = True

    for i in range(k-1):
        ij.append(A[i]+A[k-1])

    for idx in ij:
        if mark[idx]:
            find = True
    
if find:
    print("YES")
else:
    print("NO")