N, K = map(int, input().split())
primes = [ False ] * 1001
c, end = 0, False
#for i in range(2, int(N**0.5)+1):
for i in range(2, N+1):
    if end:
        break
    if not primes[i]:
        for j in range(i, N+1, i):
            if not primes[j]:
                primes[j] = True
            
                c += 1
                if c == K:
                    print(j)
                    end = True
                    break
            
            