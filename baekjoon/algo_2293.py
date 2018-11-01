N, K =map(int, input().split())
result = 0
coins = []
moneys = [ 0 for _ in range(K)]

for i in range(N):
    coins.append(int(input()))
    
coins.sort()

for i in range(N):
    if coins[i] > K:
        continue
    
    temp = coins[i]
    while temp > 0:
        moneys[K] = moneys[K - temp] + moneys[temp]
        temp -= coins[i]
    
print(moneys[K])