def gcd(a, b):
    if a % b != 0:
        return gcd(b, a % b)
    else:
        return b
        
DP = []
meetings = []
N = int(input())

for n in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key=lambda x: (x[1], x[0]))

last = -1
result = 0

for i in range(N):
    s, e = meetings[i]
    
    if last <= s:
        last = e
        result += 1 
        
print(result)
    