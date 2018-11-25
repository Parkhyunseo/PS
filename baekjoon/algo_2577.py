A = int(input())
B = int(input())
C = int(input())
text = str(A*B*C)

for i in range(10):
    print(text.count(str(i)))    
