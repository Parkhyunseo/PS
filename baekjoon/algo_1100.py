line = []
for i in range(8):
    line.append(list(input()))

count = 0

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0 and line[i][j] == 'F':
            count += 1

print(count)