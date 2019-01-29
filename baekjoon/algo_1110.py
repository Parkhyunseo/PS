N = input()
if len(N) <= 1:
    N = '0' + N

start = N
count = 0

while True:
    before = N[1]
    N = str(int(N[0])+int(N[1]))
    
    N= before+N[-1]
        
    count += 1
    if start == N:
        break
    
print(count)
    