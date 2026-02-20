replaced_word = input()
word_for_replace = input()
arr = []
with open('module-7/homework/26.02.26/task6/file.txt', 'r', encoding='utf-8') as f:
    for line in f.read().split('\n'):
        arr.append(line)

for i in range(len(arr)):
    if replaced_word in arr[i]:
        idx = arr[i].find(replaced_word)
        res1 = arr[i][:idx]
        res2 = arr[i][idx+len(replaced_word):]
        arr[i] = res1 + word_for_replace + res2
        
with open('module-7/homework/26.02.26/task6/file.txt', 'w', encoding='utf-8') as f:
    for el in arr:
        f.write(el + '\n')