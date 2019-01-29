MAX = 1000000
primes = [ True ] * (MAX+1)

for i in range(2, int(MAX**0.5)+1):
    if primes[i]:
        for j in range(i+i, MAX+1, i):
            primes[j] = False

while True:
    N = int(input())
    
    if N == 0:
        break
    
    result = 0
        
    for i in range(3, N+1, 2):
        if primes[i] and primes[N-i]:
            result = (i, N-i)
            break
                    
    print("{0} = {1} + {2}".format(N, result[0], result[1]))
"""
T = int(input())
MAX = 1000000
primes = [ True for _ in range(MAX+1)]

i = 2
while i*i <= MAX:
    if primes[i]:
        for j in range(i+i, MAX+1, i):
            primes[j] = False
            
    i += 1

while T != 0:
    chk = False
    for i in range(3, T+1, 2):
        if primes[i] and primes[T-i]:
            print("%d = %d + %d" %(T, i, T-i))
            chk = True
            break
        
    if not chk:
        print("Goldbach's conjecture is wrong.")
    T = int(input())
"""