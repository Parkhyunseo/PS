import sys

N, M = map(int, sys.stdin.readline().split())
A = []
B = []

for i in range(M):
    A.append(list(map(int, sys.stdin.readline().split())))
    
for i in range(M):
    B.append(list(map(int, sys.stdin.readline().split())))
    