X, Y = map(int, input().split())
A = min(X,Y)
B = max(X,Y)
print(B*(B+1)//2 - A*(A+1)//2 + A)
