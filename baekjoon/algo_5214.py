from queue import Queue

N, K, M = map(int, input().split())
grid = [ [] for _ in range(N) ]
hyper = []
start = []
result = 0

for i in range(M):
    line = map(lambda x: int(x) - 1, input().split())
    
    hyper[i] = line
    if line[0] == 1:
        start.append(i)
        
    for k in range(K):
        grid[line[k]].append(i) # N번 역은 i 번째 hyper tube를 탈 수 있다.

# start index의 hyper tube를 타고 시작
# 카운트도 추가
def bfs(h_index, s_index=1):
    q = Queue()
    q.put(h_index, s_index, 0)
    visit = [ False for _ in range(N) ]
    
    while q.qsize() > 0:
        cur_h, cur_s, count = q.get()
        visit[cur_s] = True
        
        if cur_s == N:
            result = count
            break
        
        for station in hyper[cur_h]:
            if visit[station]:
                continue
            else:
                for hyper in grid[station]:
                    q.put((hyper, station, count+1 if hyper != cur_h else count))
                
for s in start:
    bfs(s)
    
print(result)