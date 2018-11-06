N, K = map(int, input().split());
Q = list(map(int, input().split()));
last = [ 0 for _ in range(K)]

for i in range(N):
    available = False
    for j in range(K):
        if Q[i] > last[j]:
            last[j] = Q[i]
            available = True
            break
    if not available:
        break
  
if available:
    print("YES")
else:
    print("NO")