N = int(input())

five_count = N // 5
three_count = (N - five_count*5) // 3
remainder = ((five_count*5 + three_count*3) - N)

if N == 4 :
    five_count = -1
    three_count = 0

while remainder != 0:
    if five_count <= 0:
        if N % 3 == 0:
            five_count = 0
            three_count = N // 3
        else:
            five_count = -1
            three_count = 0
        break
    
    five_count = five_count-1
    three_count = (N - 5*five_count) // 3
    
    remainder = ((five_count*5 + three_count*3) - N)
    
print(five_count + three_count)