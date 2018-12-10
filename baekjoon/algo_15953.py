T = int(input())

table_1 = [0, 500]
table_1 += [300]*2
table_1 += [200]*3
table_1 += [50]*4
table_1 += [30]*5
table_1 += [10]*6

table_1.extend([ 0 for _ in range(80)])

table_2 = [0, 512]
table_2 += [256]*2
table_2 += [128]*4
table_2 += [64]*8
table_2 += [32]*16
table_2.extend([ 0 for _ in range(33)])

for t in range(T):
    a, b = map(int, input().split())
    
    print((table_1[a] + table_2[b])*10000)