num = list(map(int, input().split()))

result = 1000000

def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return abs(a)

def lcm(a, b):
    gcd_value = gcd(a, b)
    if gcd_value == 0:
        return 0
    return abs( (a*b) // gcd_value)
    
for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            result = min(lcm(num[k], lcm(num[i], num[j])), result)
        
print(result)
    