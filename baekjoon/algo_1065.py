N = int(input())
hansu = [ False for _ in range(1000) ]

for i in range(1, 1001):
    if i < 100:
        hansu[i-1] = True
    else:
        text = list(map(int, str(i)))
        diff = text[0] - text[1]
        flag = True
        
        for j in range(1, len(text)-1):
            if text[j] - text[j+1] != diff:
                flag = False
                break
        if flag:
            hansu[i-1] = True
                
print(hansu[:N].count(True))