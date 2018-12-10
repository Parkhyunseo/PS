N = int(input())
s = 1
for i in range(2, N+1):
    s *= i
t = str(s)[::-1]
i = 0
while t[i] == '0':
    i+=1
print(i)