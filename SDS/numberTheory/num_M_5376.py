T = int(input())

def gcd(a, b):
    if a < b :
        a, b = b, a
    return a if b == 0 else gcd(b, a%b)
    
def lcm(a, b):
    return a*b//gcd(a, b)

for t in range(T):
    n = input()
    
    if '(' in n:
        # ex) num: '0.12(34)'
        # ==> a: '12', b: '34', divisior = 9900, dividend = 1234
        a, b = n[2:-1].split('(')
        up = int(a + b) - (int(a) if a else 0)
        down = (10 ** len(a)) * (10 ** len(b) - 1)
    else:
        _, fn = n.split('.')
        up = int(fn)
        down = 10**len(fn)
        
    G = gcd(up, down)
    print(str(up//G)+'/'+str(down//G))