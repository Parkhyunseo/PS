point = -1
N, M = map(int, input().split())
mans = [ x+1 for x in range(N)]
result = []
while len(mans) > 0:
    point = (point + M) % len(mans)
    result.append(mans[point])
    del mans[point]
    point -= 1
    
print(str(result).replace("[","<").replace("]",">"))