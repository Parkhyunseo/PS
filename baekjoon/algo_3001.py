import bisect

A, B, S = map(int, raw_input().split())

# left
# 1, 140 , 6
# 910000
# 190000
# 363000
# 351000
# 자리수 부터 알아야한다
# len(str(A)) 자릿수
# list(A)해서 다 더해
# biset로 뭘 찾아야 하는가
# A[0]+A[B]
# 6,7,8,9
# 15, 16,17,18,19
# 24.........
# 105
# 114
# 123
# 
# 124
# 100, 700, 23

# A < S < B 이면 가장 작은수는 S
# S < A < B이면 S는 9로 나눠 

# 23 / 9 = 2
# 23 % 9 = 5
# 599를 찾아 먼저
# A, 599, B

# 599, B
# 