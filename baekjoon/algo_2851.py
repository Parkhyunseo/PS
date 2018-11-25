accum = []
accum.append(int(input()))
result = 0

for i in range(1, 10):
    item = int(input())
    accum.append(accum[i-1] + item)
    
for i in range(1, 10):
    if 100 - accum[i] > 0:
        result = accum[i]
    else:
        if abs(100-accum[i-1]) >= abs(100-accum[i]):
            result = accum[i]
        else:
            result = accum[i-1]
        break
    
print(result)