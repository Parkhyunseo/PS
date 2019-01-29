N = int(input())

MAX = 99999999999

d = [ 0 for _ in range(N+1)]
dp = [ [ MAX for _ in range(N+1)] for _ in range(N+1) ]
for n in range(N):
    A, B = map(int, input().split())
    
    d[n] = A
    d[n+1] = B

# dp2[a][b] => i부터 j까지 의 최소 곱 연산
for distance in range(N): # 길이 0~N-1
    for i in range(1, N-distance+1): # 여기서 부터 1~ N
        j = i + distance # 여기까지
        
        if i == j:
            dp[i][j] = 0 # 같으면 곱셈이 0 
            continue
        
        #dp[i][j] = MAX
        for k in range(i, j): # 중간 다리
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + d[i-1]*d[k]*d[j]) #  [[  ] [   ]] 이런식으로 나누어서 구간 구간의 모든 걸 다 구해
            
print(dp[1][N])