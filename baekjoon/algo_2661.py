N = int(input())
result = []

def dfs(arr):
    if len(arr) >= 2:
        half_length = len(arr)//2
        for length in range(1, half_length+1):
            if arr[len(arr) - length : len(arr)] == arr[len(arr) - 2*length : len(arr) - length]:
                return False
    
    if len(arr) == N:
        return True
    
    for i in range(1, 4):
        arr.append(i)
        result = dfs(arr)
        if result:
            return True
        else:
            arr.pop()

dfs(result)
print(''.join(str(e) for e in result))
    
