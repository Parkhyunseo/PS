import copy

N = input()
populations = map(int, raw_input().split())

towns =[ [] for _ in range(N)]

for _ in range(N-1):
    town1, town2 = map(int, raw_input().split())
    towns[town1-1].append(town2-1)
    towns[town2-1].append(town1-1)
    
result = 0

for i in range(N):
    visit = [ False for _ in range(N)]
    
    neighbour = []
    neighbour.append(i)
    temp_result = 0
    visit[i] = True
    flag = True
    
    while len(neighbour) > 0:
        nexts = []
        for town in neighbour:
            if flag:
                temp_result += populations[town]
            
            for check in towns[town]:
                if visit[check] == False:
                    nexts.append(check)
                    visit[check] = True
                    
        if flag:
            flag = False
        else:
            flag = True
        neighbour = copy.deepcopy(nexts)
        
    result = max(result, temp_result)
    
for i in range(N):
    visit = [ False for _ in range(N)]
    
    neighbour = []
    neighbour.append(i)
    temp_result = 0
    visit[i] = True
    flag = False
    
    while len(neighbour) > 0:
        nexts = []
        for town in neighbour:
            if flag:
                temp_result += populations[town]
            
            for check in towns[town]:
                if visit[check] == False:
                    nexts.append(check)
                    visit[check] = True
                    
        if flag:
            flag = False
        else:
            flag = True
        neighbour = copy.deepcopy(nexts)
        
    result = max(result, temp_result)
    
print(result)