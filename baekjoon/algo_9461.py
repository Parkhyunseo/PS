"""
d[0] => 1
d[1] => 2
d[0] + d[2] => 3
d[3] => 4
d[0] + d[4] => 5
d[1] + d[5] => 6
d[2] + d[5] => 7
d[3] + d[7] => 8
d[4] + d[8] => 9
d[5] + d[9] => 10
"""

T = int(input())
for i in range(T):
    N = int(input())
    d = [ 0 for _ in range(N if N > 5 else 5)]
    
    d[0] = 1
    d[1] = 1
    d[2] = 1
    d[3] = d[0] + d[1]
    d[4] = d[3] 
    
    for i in range(5, N):
        d[i] = d[i-1] + d[i-5]
        
    print(d[N-1])