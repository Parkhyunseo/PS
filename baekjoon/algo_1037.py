N = input()
divisors = [ int(x) for x in input().split()]
low = min(divisors)
high = max(divisors)
print(low*high)
