from functools import lru_cache

N = int(input())
A = [ int(x) for x in input().split() ]
visited = [ False for _ in range(N+1)]

op, A = A[0], A[1:]

@lru_cache(maxsize=20)
def f(n):
    #if n <= 0:
    #    return 0
    
    return 1 if n <= 1 else n*f(n-1)

#  k번째 순열
if op == 1:
    find = A[0] # 찾는 K
    result = []
    
    for i in range(N, 0, -1): #  자릿수
        for j in range(1, N+1): # 순열 수
            if not visited[j]:
                if find <= f(i-1):
                    result.append(str(j))
                    visited[j] = True
                    break
                else:
                    find -= f(i-1)
                
    print(' '.join(result))
# 몇 번째 순열인가
else:
    point = N-1
    result = 0
    
    for a in A:
        count = 0
        for i in range(1, N+1):
            if not visited[i]:
                if a == i:
                    result += count
                    visited[i] = True
                    point -= 1
                    break
                else:
                    #print('{0}가 없다. {1}증가, {2}'.format(i, f(point), result))
                    count += f(point)
                
    print(result+1)
                
"""
F(2) = 2
F(!) = 1
F(0) = 1

1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""