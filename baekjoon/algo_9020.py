import bisect
T = int(input())

prime_table = [ False for _ in range(10001) ]
primes = []

def che():
    for i in range(2, 10001):
        if prime_table[i] == False:
            for j in range(2*i, 10001, i):
                prime_table[j] = True
                
    for i in range(2, 10001):
        if not prime_table[i]:
            primes.append(i)

#def get_partition(N):
che()

for t in range(T):
    N = int(input())
    result = [0, 0]
    min_sub = N
    for i in range(2, N//2+1):
        if prime_table[i]:
            continue
    
        if not prime_table[N-i]:
            sub = N - 2*i
            if sub < min_sub:
                min_sub = sub
                result[0] = i
                result[1] = N-i
    print(result[0], result[1])