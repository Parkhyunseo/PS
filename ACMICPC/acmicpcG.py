N, K = map(int, input().split());
Q = list(map(int, input().split()));
last = [ 0 for _ in range(K)]
for n in range(N):
 available = True
 for k in range(K):
  if(last[k] < Q[n]):
   last[k] = Q[n]
  else:
   available = False
   break
if available:
 print("YES")
else:
 print("NO")