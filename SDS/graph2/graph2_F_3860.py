from sys import stdin

cemeterys = [ False ] * 91
MAX = 100000000

W, H = map(int, stdin.readline().split())

G = stdin.read()

adj = [ [MAX] * 91] * 91

#BFS로 인접한 애들은 T을 1로 초기화
# 잔디
for g in range(W*H):
    for j in range(W*H):

for g in range(G):
    x, y = map(int, stdin.readline().split())
    cemeterys[W*(y)+x] = True
    
E = stdin.read()

for e in range(E):
    in_x, in_y , out_x, out_y, t = map(int, stdin.readline().split())
    adj[W*(in_y-1)+in_x][W*(out_y-1)+out_x] = t
    
for v in range(W*H-1):
    for e in range((W*H-1)) * W*H):
        if cemeterys[e]:
            continue
        if adj[]


