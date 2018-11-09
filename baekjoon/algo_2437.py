N = int(input())
W = map(int, input().split())

W.sort()
# N/2 만큼 서치
for i in range(N):
    for j in range(N):
        W[i] ==