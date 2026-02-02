fruit = input()
fr = ('apple-banana', 'apple', 'bananamango')
c = 0
for el in fr:
    if fruit in el:
        c += 1
print(c)