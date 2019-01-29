N = int(input())
arr = []

for i in range(N):
    arr.append([int(x) for x in input().split()])
            
max_a = max_b = max_c = 0
min_a = min_b = min_c = 0

for i in range(N):
    max_d = max(max_a + arr[i][0], max_b + arr[i][0])
    max_e = max(max_a + arr[i][1], max_b + arr[i][1], max_c+ arr[i][1])
    max_f = max(max_b + arr[i][2], max_c + arr[i][2])
    
    min_d = min(min_a + arr[i][0], min_b + arr[i][0])
    min_e = min(min_a + arr[i][1], min_b + arr[i][1], min_c+ arr[i][1])
    min_f = min(min_b + arr[i][2], min_c + arr[i][2])
    
    max_a, max_b, max_c = max_d, max_e, max_f
    min_a, min_b, min_c = min_d, min_e, min_f
    
print(max(max_a, max_b, max_c), min(min_a, min_b, min_c))