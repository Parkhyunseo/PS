#-*- coding:utf-8 -*-
import bisect

N, H = map(int, raw_input().split())
stalagmites = [] 
stalactites = []

for i in range(N):
    if i & 1 == 0:
        stalagmites.append(input())
    else:
        stalactites.append(input())

stalagmites.sort()        
stalactites.sort()

print stalagmites
print stalactites

results = []

for i in range(1, H+1):
    print str(i) + "번 째"
    count = 0
    found = bisect.bisect_left(stalagmites, i)
    
    if found < len(stalagmites):
        if stalagmites[found] == i:
            count += 1
        elif stalagmites[0] > i:
            count += 1
            
        count += len(stalagmites) - found -1
        print str(i) + "종유석 : " + str(count)
    
    found = bisect.bisect_left(stalactites, H+1-i)
    
    if found < len(stalactites):
        if stalactites[found] == H+1-i:
            count += 1
        elif stalactites[0] > i:
            count += 1
            
        count += len(stalactites) - found -1
        print str(i) + "최종 : " + str(count)
        
    results.append(count)
        
results.sort()
result = results[0]
count = 0

print results

for value in results:
    if value == result:
        count += 1
    else:
        break
    
print str(result) + " " + str(count)