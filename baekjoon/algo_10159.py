N = input()
M = input()

G = [ [ 0 if i !=j else 1 for j in range(N) ] for i in range(N)]

for m in range(M):
    (f, t) = map(int, raw_input().split())
    G[f-1][t-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if G[i][k] + G[k][j] == 2:
                G[i][j] = 1

for i in range(N):
    count = 0
    for j in range(N):
        if G[i][j] == 1 or G[j][i] == 1:
            count += 1
            
    print N-count
