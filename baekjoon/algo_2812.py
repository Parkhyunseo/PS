import bisect

N, K = map(int, input().split())
num = list(map(int, list(input())))

sorted_num = sorted(num)
#print(sorted_num)
base = sorted_num[K-1]
left = bisect.bisect_left(sorted_num, base)
right = bisect.bisect_right(sorted_num, base)

count = N-(N-right)-K

#print(left)
#print(count)
#print(left)
#print(right)

result = ''

for i in range(N):
    if base < num[i]:
        result += str(num[i])
    elif base == num[i]:
        if count > 0:
            result += str(num[i])
            count -=1

print(result)

stack = []
stack.append(num[0])
for i in range(1, N):
    if len(stack) == 0:
        stack.append(num[i])
        continue
    
    if stack[-1] >= num[i]:
        stack.append(num[i])
    else:
        if len(stack) + N-1 -i  > N-K: 
            while len(stack) > 0:
                temp = stack.pop()
                if temp > num[i]:
                    stack.append(temp)
                    stack.append(num[i])
                    break
        else:
            stack.append(num[i])
                
                
print(stack)