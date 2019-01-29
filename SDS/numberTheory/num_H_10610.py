l=sorted([int(x) for x in list(input())],reverse=True)
s,c=sum(l),l[-1]
if s%3 == 0 and c == 0:
    for a in l:
        print(a, end='')
    print('')
else:
    print(-1)