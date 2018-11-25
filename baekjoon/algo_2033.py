N = int(input())
pos = 1

while N > 10**pos:
    if N % int(10**pos) >= 5 * 10**(pos-1):
        N += 10**pos
        
    N -= N % 10**pos
    
    pos+=1
    
print(N)