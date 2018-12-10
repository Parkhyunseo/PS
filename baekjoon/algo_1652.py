N = int(input())
room = []
for i in range(N):
    room.append(list(input()))
    
horizontal = 0
vertical = 0

for i in range(N):
    count = 0
    for j in range(N):
        if room[j][i] == 'X':
            count = 0
        else:
            count += 1
        
        if count == 2:
            horizontal += 1

for i in range(N):
    count = 0
    for j in range(N):
        if room[i][j] == 'X':
            count = 0
        else:
            count += 1
        
        if count == 2:
            vertical += 1
            
print(vertical, horizontal)
            
        