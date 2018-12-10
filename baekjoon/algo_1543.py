S = input()
F = input()

p = 0
last_p = len(S)-len(F)
count = 0

while p <= last_p:
    if F == S[p:p+len(F)]:
        count += 1
        p += len(F)
    else:
        p += 1
    
print(count)