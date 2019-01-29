T = int(input())

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

for t in range(T):
    K, C = map(int, input().split())
    
    # 최소 10억 1개
    if gcd(K, C):
        
