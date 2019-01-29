from sys import stdin
import math

N = int(stdin.readline())

MAX_NODE = 100001

graph = [ [] for _ in range(MAX_NODE)]
depth = [ 0 for _ in range(MAX_NODE)]
dp = [ [ 0 for _ in range(20)] for _ in range(MAX_NODE)]

max_level = 0

# Step 1. dp 구하기
def get_dp(here, parent):
    global max_level
    depth[here] = depth[parent] + 1
    
    dp[here][0] = parent
    
    max_level = int(math.floor(math.log(MAX_NODE, 2)))
    
    for i in range(1, max_level+1):
        tmp = dp[here][i-1]
        dp[here][i] = dp[tmp][i-1]
    
    for there in graph[here]:
        if there != parent:
            get_dp(there, here)

# make dp
for n in range(N-1):
    f, t = map(int, stdin.readline().split())
    graph[f].append(t)
    graph[t].append(f)

depth[0] = -1

get_dp(1, 0)

M = int(stdin.readline())

for m in range(M):
    node_a, node_b = map(int, stdin.readline().split())
    
    # Step.2 높이 맞추기
    if depth[node_a] != depth[node_b]:
        # node_a가 depth가 더 작아야한다
        if depth[node_a] > depth[node_b]:
            node_a, node_b = node_b, node_a
        
        # for 문이 끝나면  depth가 같아진다
        for i in range(max_level, -1,-1):
            if depth[node_a] <= depth[dp[node_b][i]]:
                node_b = dp[node_b][i]
    
    lca = node_a
    
    # Step.3 LCA 구하기
    if node_a != node_b:
        for i in range(max_level, -1, -1):
            if dp[node_a][i] != dp[node_b][i]:
                node_a = dp[node_a][i]
                node_b = dp[node_b][i]
            
            lca = dp[node_a][i]
        
    print(lca)
    
    

    

    

