word = input()
arr = []
with open('module-7/homework/26.02.26/task5/file.txt', 'r', encoding='utf-8') as f:
    for line in f.read().split('\n'):
        arr.append(line)

s = ''.join(arr)
print(s.count(word))