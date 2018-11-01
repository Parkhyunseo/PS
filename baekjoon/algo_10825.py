N = input()
students = []

for i in xrange(N):
    student = raw_input().split()
    name, score = student[0], map(int, student[1:])
    score.insert(0, name)
    students.append(score)
    
rank = sorted(students, key=lambda x : (-x[1], x[2], -x[3], x[0]) )

for i in xrange(len(rank)):
    print rank[i][0]
    