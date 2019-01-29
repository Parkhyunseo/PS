a,b = map(int, input().split())
c,d = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
    
def lcm(a, b):
    return a*b//gcd(a,b)
    
denominator = lcm(b,d)
numerator = denominator//b * a + denominator//d * c
divide = gcd(denominator, numerator)
print(numerator//divide, denominator//divide)