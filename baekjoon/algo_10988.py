text = raw_input()

end_point = int(len(text)/2)
result = 1

for i in range(end_point+1):
    if text[i] != text[-(i+1)]:
        result = 0
        break
    
print result
    