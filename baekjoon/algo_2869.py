#A, B, V = map(int, raw_input().split())
#X = (V-A) / (A-B)
#if V == A:
#    print(1)
#else:
#    print(X+1)

A, B, V = map(int, input().split())

X = (V-A) // (A-B) 
mod = (V-A) % (A-B)

if mod != 0:
    X += 2
else:
    X += 1
print(X)