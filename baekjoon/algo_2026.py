K, N, F = map(int, input().split())

relation = [ [ 0 for _ in range(N) ] for _ in range(N)]
tree = [ [] for _ in range(N)]
stack = []
result = False

for f in range(F):
    a, b = map(lambda x:int(x)-1, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def dfs()-> bool: 
    global result
    
    if result:
        return
    
    if len(stack) == K:
        result = True
        for item in stack:
            print(item+1)
        return
    
    here = stack[-1]
    visit[here] = True
        
    for i in range(len(tree[here])):
        there = tree[here][i]
        
        if visit[there]:
            continue
        
        no = False
        for s in stack:
            if relation[s][there] == 0:
                no = True
                break
            
        if not no:
            stack.append(there)
            dfs()
            stack.pop()
       
for i in range(N):
    visit = [ False for _ in range(N)]
    if not result:
        stack.append(i)
        dfs()
        stack.pop()

if not result:
    print("-1")

            
            
    