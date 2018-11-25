N=int(input())
for i in range(N):
    for j in range(N-i-1):
        print(" ", end="")
    print("*"*(2*i+1))
for i in reversed(range(N-1)):
    for j in range(N-i-1):
        print(" ", end="")
    print("*"*(2*i+1))
