N = int(input())
T, P = [0], [0]
#d = [ 0 for _ in range(N+1)] # i일 까지의 최고 수익 전날에 j를 선택 했을 때

for i in range(N):
    ti, pi = map(int, input().split())
    T.append(ti)
    P.append(pi)

d = [ P[i] for i in range(N+1)]
   
for i in range(2, N + 1):
    for j in range(1, i):
        #if j + T[j] >= i:
        #    continue
        if i - j >= T[j]:
            d[i] = max(d[i], d[j] + P[i])

result = 0
for i in range(1, N+1):
    if i + T[i] <= N+1:
        result = max(result, d[i])
    

print(result)