N, K =map(int, input().split())
coins = [ 0 ]
moneys = [ 0 for _ in range(K+1)]
moneys[0]=1

for i in range(N):
    coins.append(int(input()))

for i in range(1, N+1):
    for j in range(1, K+1):
        if j-coins[i] >= 0:
            moneys[j] += moneys[j-coins[i]];
        
print(moneys[K])