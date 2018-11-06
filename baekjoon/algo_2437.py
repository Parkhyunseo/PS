N = int(input())
W = map(int, input().split())

W.sort()

for i in range(N):
    for j in range(N):
        