N = int(input())
count = 0

def move(n, src, used, dst, is_print):
    global count
    count += 1

    if n == 1:
        if is_print:
            print(src, dst)
    else:
        move(n-1, src, dst, used, is_print)
        if is_print:
            print(src, dst)
        move(n-1, used, src, dst, is_print)

if N <= 20:
    print(2**N-1)
    move(N, 1, 2, 3, N <= 20)
else:
    print(2**N-1)
