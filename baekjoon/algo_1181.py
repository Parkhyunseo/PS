N = input()
words = set()

for i in xrange(N):
    words.add(raw_input())

words = list(words)
result = sorted(words, key=lambda x : (len(x), x))

for i in xrange(len(result)):
    print(result[i])
    