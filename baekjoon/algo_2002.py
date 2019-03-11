N = int(input())

incars = []
outcars = []

for n in range(N):
    incars.append(input())
    
for n in range(N):
    outcars.append(input())
    
while len(outcars) > 0:
    incar = incars.pop(0)
    outcar = outcars.pop(0)
    if incar != outcar:
        incars.insert(0, incar)
        incars.append(incar)
        while True:
            nextcar = incars.pop(0)
            if nextcar == outcar:
                break
            else:
                incars.append(nextcar)
                
print(len(incars))