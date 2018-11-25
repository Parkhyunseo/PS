H, M = map(int, input().split())
diff = M-45
M = 60+diff if diff < 0 else diff
if diff < 0:
    H = 23 if H-1 < 0 else H-1
print(H, M)
