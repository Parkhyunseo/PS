a, b, n, w = map(int, input().split())

count = 0
sheep = 0
goat = 0

for i in range(1, n):
    x, y = i, n-i
    
    if w == a*x+ b*y:
        count += 1
        sheep = x
        goat = y
        
if count == 0 or count >= 2:
    print(-1)
else:
    print(sheep, goat)