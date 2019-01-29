T = int(input())

for t in range(T):
    answer = input()
    
    count = 0
    result = 0
    for s in answer:
        if s == 'O':
            count += 1
            result += count
        else:
            count = 0
    
    print(result)