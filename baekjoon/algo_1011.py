#-*- coding:utf-8 -*-
# 한 칸 전은 1이어야 하니까
from math import ceil
T=int(input())

for _ in range(T):
    x, y = map(int ,input().split())

    dist = y - x
    
    jump = 1
    while True:
        if jump**2 > dist:
            break
        jump+=1
        
    jump -=1
    
    left = dist - jump**2
    left = ceil(left/jump)
    
    print(jump*2 - 1 + left)
    