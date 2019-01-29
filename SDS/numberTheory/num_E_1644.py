MAX = 4000000
primes = [ True ] * (MAX+1)
pl = []

for i in range(2, int(MAX**0.5)+1):
    if primes[i]:
        for j in range(i+i, MAX+1, i):
            primes[j] = False

for i in range(2, MAX+1):
    if primes[i]:
        pl.append(i)

primes.sort()
N = int(input())

left = 0
right = 0
total = 0
count = 0

while True:
    if total >= N:
        total -= pl[left]
        left += 1
    elif right >= len(pl):
        break
    else:
        total += pl[right]
        right += 1
        
    if total == N:
        count += 1

print(count)