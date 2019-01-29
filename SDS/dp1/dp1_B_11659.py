N, M = map(int, input().split())
A = [ int(x) for x in input().split()]
accum = [A[0]]
for i in range(1, N):
    accum.append(accum[-1] + A[i])
    
for _ in range(M):
    l,r = map(int, input().split())
    print(accum[r-1]-accum[l-1]+A[l-1])