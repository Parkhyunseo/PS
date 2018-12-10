N = int(input())
x = 1
count = 0
while True:
    x += 6*count
    count += 1
    if x >= N:
        break
print(count)
    