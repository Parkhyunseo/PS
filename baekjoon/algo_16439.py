from sys import stdin

N, M = map(int, stdin.readline().split())

preferences = []
result = 0

for i in range(N):
    preferences.append(list(map(int, stdin.readline().split())))
    
def dfs(stack: list):
    if len(stack) >= 3:
        global result
        temp = 0
        for i in range(N):
            temp += max(preferences[i][stack[0]], preferences[i][stack[1]], preferences[i][stack[2]])
        result = max(result, temp)
        return
    
    for i in range(M):
        #print(stack)
        stack.append(i)
        dfs(stack)
        stack.pop()
        
dfs([])   
print(result)

    