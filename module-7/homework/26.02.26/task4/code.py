arr = []
with open('module-7/homework/26.02.26/task4/file.txt', 'r', encoding='utf-8') as f:
    for line in f.read().split('\n'):
        arr.append(line)

m = 0
for el in arr:
    if len(el) > m:
        m = len(el)


print(m)
