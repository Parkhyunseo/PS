N = int(input())

queens = []
count = 0

def dfs():
    global count
    if len(queens) >= N:
        count += 1
        return
    
    for col in range(N):
        if check(col):
            queens.append(col)
            dfs()
            queens.pop()

        
def check(here):
    for i in range(len(queens)):
        if queens[i] == here:
            return False
        elif abs(queens[i]-here) == abs(len(queens)-i):
            return False
            
    return True
            
dfs()
print(count)