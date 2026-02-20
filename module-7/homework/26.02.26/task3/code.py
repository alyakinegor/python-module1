arr = []
with open('module-7/homework/26.02.26/task3/example.txt', 'r', encoding='utf-8') as f:
    for line in f.read().split('\n'):
        arr.append(line)

with open('module-7/homework/26.02.26/task3/result.log', 'w', encoding='utf-8') as r:
    for el in arr[:-1]:
        r.write(el+'\n')
    