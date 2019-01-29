from math import *;N, K = map(int, input().split())
print(factorial(N)//factorial(N-K)//factorial(K))

