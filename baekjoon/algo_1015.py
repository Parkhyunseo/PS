N = int(input())
A = list(map(int, input().split()))
A = list(zip(A, range(N)))

A.sort(key= lambda x: x[0])

P = [ 0 for _ in range(N)]
k = 0
for v, i in A:
    P[i] = k
    k += 1

print(' '.join(str(x) for x in P))

