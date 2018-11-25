N = int(input())
teams = list(map(int, input().split()))
teams.insert(0, 0)
flag = False
teams.sort()
for i in range(1, N+1):
    if teams[i] > N-i or teams[i] < 0:
        flag=True
        print("-1")
        break
    
    for j in range(1, N-teams[i]):
        teams[N-j] -= 1
    teams.sort()
        
if not flag:
    print("1")