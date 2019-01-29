from sys import stdout
MAX = 10000000
primes = [ True ] * (MAX+1)
pl = []

for i in range(2, int(MAX**0.5)+1):
    if primes[i]:
        for j in range(i+i, MAX+1, i):
            primes[j] = False

for i in range(2, MAX+1):
    if primes[i]:
        pl.append(i)

N = int(input())
pointer = 0

while True:
    if pointer >= len(pl) or N <= 1:
        break
    
    if N % pl[pointer] == 0:
        stdout.write(str(pl[pointer])+'\n')
        N = N // pl[pointer]
    else:
        pointer += 1

