N = input()
coordinate = []

for i in range(N):
    coordinate.append(map(int, raw_input().split()))
    
results = sorted(coordinate, key=lambda x: (x[1], x[0]))

for result in results:
    print str(result[0]) + " " + str(result[1])