arr1 = []
arr2 = []
with open('module-7/homework/26.02.26/task1/file1.txt', 'r', encoding='utf-8') as f:
    for line in f.read().split('\n'):
        arr1.append(line)

with open('module-7/homework/26.02.26/task1/file2.txt', 'r', encoding='utf-8') as f2:
    for line in f2.read().split('\n'):
        arr2.append(line)
for i, j in zip(arr1, arr2):
    if i != j:
        print(f'не совпадают в file1: {i}, file2: {j}')