def get_manhatten_distance(f, t):
    x1, y1 = f
    x2, y2 = t
    return abs(x2-x1) + abs(y2-y1)

def solve(depth, before):
    global result
    
    if depth == M:
        #치킨집의 최소 거리의 합을 구해라    
        total = 0
        for home in homes:
            dist = MAX
            for i in range(len(chickens)):
                if checked[i]:
                    dist = min(dist, get_manhatten_distance(home, chickens[i]))
                    
            total += dist
        result = min(result, total)
        return

    for i in range(before+1, len(chickens)):    
        if not checked[i]:
            checked[i] = True
            solve(depth+1, i)
            checked[i] = False

# M개의 치킨집만 남겨놓는다.
N, M = map(int, input().split())
MAX = 100000

grid = [ [ 0 for _ in range(N)] for _ in range(N)]
homes = []
chickens = []
result = MAX

for i in range(N):
    line = [ int(x) for x in input().split()]
    for j in range(N):
        if line[j] == 2:
            chickens.append((j, i))
        if line[j] == 1:
            homes.append((j, i))
        grid[i][j] = line[j]

checked = [ False for _ in range(len(chickens))]

solve(0, -1)

print(result)
            

    
    