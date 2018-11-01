import copy

dwarfs = []
result = []
for i in range(9):
    dwarfs.append(int(input()))
    
def dfs(visit):
    if len(visit) == 7:
        if sum(visit) == 100:
           global result
           result = copy.deepcopy(visit)
        return
    
    for i in range(9):
        if dwarfs[i] not in visit:
            visit.append(dwarfs[i])
            dfs(visit)
            visit.pop()

for i in range(9):
    dfs([dwarfs[i]])
    
for r in sorted(result):
    print(r)
#print(sorted(result))