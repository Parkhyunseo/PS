N = int(input())
primes = []
radix = 10**(N-1)

def is_prime(num):
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    
    return True

def dfs(num, count):

    # 이 숫자가 소수인가
    if is_prime(num) == False:
        return
    
    if count == N:
        print(num)
        return
    
    for i in range(10):
        dfs(int(str(num) + str(i)), count+1)
        

for i in range(2, 10):
    dfs(i,1)
    
"""
def preprocess_prime(exponent):
    radix = 10 ** (n-1)
    
    for i in range(radix):
        for prime in primes:
            if prime  
            if num // i == 0:
                primes.append(num)
"""


    
    