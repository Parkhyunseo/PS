P, K = map(int, input().split())

MAX = 1000000

primes = [ True ] * (MAX+1)

find = False

for i in range(2, int(MAX**0.5)+1):
#for i in range(2, MAX+1):    
    if primes[i]:
        for j in range(i+i, MAX+1, i):
            primes[j] = False

# pq, p or q < K

#print(primes)

for k in range(2, K):
    if primes[k]:
        if P % k == 0:
            find = True
            print("BAD", k)
            break
            
if not find:
    print("GOOD")