A, B = map(list, input().split())
b_sum = sum([int(x) for x in B])
s = 0
for i in range(len(A)):
    s += int(A[i])*b_sum
print(s)