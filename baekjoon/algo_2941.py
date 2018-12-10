text = input()
alpha = ['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
i = 0
count = 0
for a in alpha:
    count += text.count(a)
    text = text.replace(a,"@")
text = text.replace("@", "")
count += len(text)
print(count)