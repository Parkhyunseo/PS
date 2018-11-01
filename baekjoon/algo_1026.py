N = input()
A = map(int, raw_input().split())
B = map(int, raw_input().split())
B.sort(reverse=True)
A.sort()

S = 0
for n in xrange(N):
    S += A[n]*B[n]
    
print(S)