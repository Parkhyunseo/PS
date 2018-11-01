N = int(input())

grades = list(map(int, input().split()))
AVG = 0
SUM = 0

AVG = sum(grades) / len(grades)
MAX = max(grades)

for grade in grades:
    SUM += (grade / MAX) * 100

print(SUM/len(grades))