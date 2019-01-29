from sys import stdin
V, E = map(int, stdin.readline().split())

graph = [ [] for _ in range(V+1)]
order = [ 0 for _ in range(V+1) ]
iscut = [ False for _ in range(V+1)]

count = 0

def find(here, is_root):
    global count 
    
    count += 1
    order[here] = count
    
    
    child_count = 0
    
    min_order = order[here]
    
    for child in graph[here]:
        if order[child] != 0:
            min_order = min(min_order, order[child])
            continue
        
        child_count += 1
        
        prev = find(child, False)
            
        if not is_root and prev >= order[here]:
            iscut[here] = True
            
        min_order = min(prev, min_order)
    
    if is_root:
        if child_count >= 2:
            iscut[here] = True
    
    return min_order

for e in range(E):
    f, t = map(int, stdin.readline().split())
    graph[f].append(t)
    graph[t].append(f)
    
for i in range(1, V+1):
    if order[i] == 0:
        find(i, True)

print(iscut.count(True))

result = []
for i in range(1, V+1):
    if iscut[i]:
        result.append(str(i))
print(' '.join(result))

