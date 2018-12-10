import sys;s=0;m=101;a=map(int,sys.stdin.readlines());
for n in a:
    if n & 1 is 1:
        s+=n
        m = min(m,n)
if s is not 0:
    print("%d\n%d"%(s,m))
else:
    print(-1)