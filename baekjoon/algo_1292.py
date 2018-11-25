A, B = map(int, input().split())

def sum_section(x: int) -> int:
    result = 0
    num = 0
    
    for i in range(1, 1001):
        if i*(i+1)/2 >= x:
            num = i
            break

    for i in range(num):
        result += i*i
    
    result += num*(x-num*(num-1)//2)
    return result

print(sum_section(B)-sum_section(A-1))
