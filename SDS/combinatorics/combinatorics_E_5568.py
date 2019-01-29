N = int(input()); K=int(input())
arr = []
for n in range(N):
    arr.append(int(input()))
    
visited = [ False for _ in range(10)]
result = set()

def solve(text, count):
    if count == K:
        result.add(text)
    
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            solve(text+str(arr[i]), count+1)
            visited[i] = False

solve('', 0)
print(len(result))

    
    