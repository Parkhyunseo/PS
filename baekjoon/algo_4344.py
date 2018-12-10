T = int(input())

for t in range(T):
    N, *score = map(int, input().split())
    average = sum(score) / N
    count = 0
    for s in score:
        if s > average:
            count += 1
            
    print("%.3f" % (count *100 / N) + "%")