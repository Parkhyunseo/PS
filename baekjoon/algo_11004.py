N, K = map(int, input().split())
A = map(int, input().split())#[ int(x) for x in input().split() ])
print(sorted(A)[K-1])